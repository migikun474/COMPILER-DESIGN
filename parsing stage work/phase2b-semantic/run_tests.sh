#!/bin/bash
# Usage: ./run_tests.sh [path-to-semantic_analyzer]
#
# Self-checking semantic test suite.
#
#   test/valid/*.c    must be accepted (exit 0)
#   test/invalid/*.c  must be rejected (exit 1)
#
# Every diagnostic a test expects is written on the source line where it
# must be reported, as a trailing comment:
#
#     x = 10;            // error: undeclared identifier 'x'
#     printf("%d\n");    // warning: expects 1 argument
#     void main(int x) {  // error: must return 'int'  // error: invalid parameter list
#
# The text after "error:"/"warning:" must appear (case-insensitively) in
# a semantic or preprocessor diagnostic of that kind reported on that line. Any diagnostic the
# file does not announce is a failure too, so spurious errors are caught
# as reliably as missing ones.
#
# A declaration may also announce its link name (Itanium C++ ABI):
#
#     int over(double a) { return 0; }    // mangled: _Z4overd
#
# Both symbol tables (parser and semantic) must then contain exactly the
# announced names.
#
# Finally the parser's own corpus (../phase2-parser/test) is run end to
# end: syntactically valid programs must pass semantic analysis, programs
# with syntax errors must stop before it.

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
EXEC="${1:-$SCRIPT_DIR/semantic_analyzer}"
PARSER_TESTS="$SCRIPT_DIR/../phase2-parser/test"
PARSER="$SCRIPT_DIR/../phase2-parser/syntax_analyzer"

if [ ! -x "$EXEC" ]; then
    echo "Error: executable '$EXEC' not found or not executable. Build it first with 'make'."
    exit 1
fi

pass=0
fail=0
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

# check_file <file> <expected exit code>
check_file() {
    local f="$1" want="$2" out code
    out="$("$EXEC" -q "$f" 2>&1)"
    code=$?

    # expected: "line<TAB>kind<TAB>text"; a dummy first row keeps awk's
    # two-file idiom working when a file expects nothing
    printf '0\tnone\tnone\n' > "$TMP/expected"
    awk '{
        line = $0
        while (match(line, /\/\/[ \t]*(error|warning):/)) {
            kind = (substr(line, RSTART, RLENGTH) ~ /error/) ? "error" : "warning"
            rest = substr(line, RSTART + RLENGTH)
            if (match(rest, /\/\/[ \t]*(error|warning):/)) { text = substr(rest, 1, RSTART - 1); line = substr(rest, RSTART) }
            else { text = rest; line = "" }
            gsub(/^[ \t]+|[ \t]+$/, "", text)
            print FNR "\t" kind "\t" text
        }
    }' "$f" >> "$TMP/expected"
    printf '%s\n' "$out" |
        sed -n -E 's#^.*:([0-9]+):[0-9]+: (semantic|preprocessor) (error|warning): (.*)$#\1\t\3\t\4#p' > "$TMP/actual"

    local report
    report="$(awk -F'\t' '
        FNR == NR { if ($1 != 0) { el[++ne] = $1; ek[ne] = $2; et[ne] = tolower($3) } next }
        { dl[++nd] = $1; dk[nd] = $2; dt[nd] = tolower($3) }
        END {
            for (i = 1; i <= ne; i++) {
                found = 0
                for (j = 1; j <= nd; j++)
                    if (!used[j] && dl[j] == el[i] && dk[j] == ek[i] && index(dt[j], et[i]) > 0) { used[j] = 1; found = 1; break }
                if (!found) printf "    missing %s on line %s: \"%s\"\n", ek[i], el[i], et[i]
            }
            for (j = 1; j <= nd; j++)
                if (!used[j]) printf "    unexpected %s on line %s: %s\n", dk[j], dl[j], dt[j]
        }' "$TMP/expected" "$TMP/actual")"

    # name mangling: a declaration annotated `// mangled: NAME` must get
    # exactly that link name, in the semantic table and in the parser's
    # table alike, and no other mangled name may appear
    if grep -q "// mangled:" "$f"; then
        grep -o "// mangled: [A-Za-z0-9_]*" "$f" | awk '{print $3}' | grep '^_Z' | sort -u > "$TMP/mexp"
        "$EXEC" "$f" 2>/dev/null | awk '/=== Semantic Symbol Table/{t=1} t&&/^=== Record/{t=0} t' |
            grep -oE '_Z[A-Za-z0-9_]+' | sort -u > "$TMP/msem"
        "$PARSER" "$f" 2>/dev/null | grep -oE '_Z[A-Za-z0-9_]+' | sort -u > "$TMP/mpar"
        local which
        for which in sem par; do
            local label=$([ "$which" = sem ] && echo "semantic table" || echo "parser table")
            local m
            m="$(comm -23 "$TMP/mexp" "$TMP/m$which" | sed "s/^/    missing mangled name ($label): /"
                 comm -13 "$TMP/mexp" "$TMP/m$which" | sed "s/^/    unexpected mangled name ($label): /")"
            [ -n "$m" ] && report="${report:+$report$'\n'}$m"
        done
    fi

    if [ "$code" -ne "$want" ]; then
        report="    exit code $code, expected $want"$'\n'"$report"
        if [ -z "$(cat "$TMP/actual")" ]; then report="$report"$'\n'"$(printf '%s\n' "$out" | head -5 | sed 's/^/    | /')"; fi
    fi
    if [ -z "$report" ]; then
        pass=$((pass + 1))
        printf '  PASS  %s\n' "${f#$SCRIPT_DIR/}"
    else
        fail=$((fail + 1))
        printf '  FAIL  %s\n%s\n' "${f#$SCRIPT_DIR/}" "$report"
    fi
}

echo "=== semantic tests: valid programs ==="
for f in "$SCRIPT_DIR"/test/valid/*.c; do check_file "$f" 0; done
echo
echo "=== semantic tests: invalid programs ==="
for f in "$SCRIPT_DIR"/test/invalid/*.c; do check_file "$f" 1; done

# Parser corpus. Syntactically valid programs that semantic analysis
# must reject:
#  - operators.c line 11, `c = a+++++b;`, lexes as `(a++)++ + b`,
#    incrementing an rvalue -- gcc and g++ reject it with the same
#    "lvalue required as increment operand".
#  - test7_cpp_features.c line 35, `Dog d;`, where Dog's only
#    constructor is Dog(int): g++ rejects it ("no matching function for
#    call to 'Dog::Dog()'"). It was written when the grammar could not
#    call constructors with arguments at all; now `Dog d(4);` works.
declare -A CORPUS_EXPECT=(
    [operators.c]="lvalue required as increment operand"
    [test7_cpp_features.c]="has no default constructor"
)
echo
echo "=== end to end: phase2-parser corpus through semantic analysis ==="
for f in "$PARSER_TESTS"/*.c; do
    name="$(basename "$f")"
    out="$("$EXEC" -q "$f" 2>&1)"
    code=$?
    if printf '%s' "$out" | grep -q "semantic analysis was not run"; then
        verdict="syntax errors -> semantic analysis skipped"
        ok=$([ "$code" -eq 1 ] && echo 1)
    elif [ -n "${CORPUS_EXPECT[$name]}" ]; then
        verdict="rejected: ${CORPUS_EXPECT[$name]}"
        ok=$([ "$code" -eq 1 ] && printf '%s' "$out" | grep -q "${CORPUS_EXPECT[$name]}" && echo 1)
    else
        verdict="accepted"
        ok=$([ "$code" -eq 0 ] && echo 1)
    fi
    if [ -n "$ok" ]; then
        pass=$((pass + 1))
        printf '  PASS  %-48s %s\n' "$name" "$verdict"
    else
        fail=$((fail + 1))
        printf '  FAIL  %-48s expected: %s (exit %s)\n' "$name" "$verdict" "$code"
        printf '%s\n' "$out" | grep -E "semantic (error|warning)" | head -5 | sed 's/^/    | /'
    fi
done

echo
echo "passed: $pass   failed: $fail"
[ "$fail" -eq 0 ]
