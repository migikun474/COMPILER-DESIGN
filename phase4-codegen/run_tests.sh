#!/bin/bash
# Usage: ./run_tests.sh
#
# Compiles every ../phase3-ir/test/*.c to MIPS (without optimization,
# with -O1 and with -O2), runs the result in SPIM and compares what the
# program prints, and its exit code, with the same expected file the TAC
# interpreter is checked against (../phase3-ir/test/expected/<name>.out,
# verified against gcc/g++).

cd "$(dirname "${BASH_SOURCE[0]}")" || exit 1
[ -x ./mips_generator ] || { echo "Build it first with 'make'."; exit 1; }
command -v spim > /dev/null || { echo "spim is not installed (sudo apt install spim)."; exit 1; }
T=../phase3-ir/test
TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
pass=0; fail=0
for f in $T/*.c; do
    n="$(basename "$f" .c)"
    args=""; [ -f "$T/$n.args" ] && args="$(cat "$T/$n.args")"
    in=/dev/null; [ -f "$T/$n.in" ] && in="$T/$n.in"
    ok=1; note=""
    for level in -O0 -O1 -O2; do
        ./mips_generator $level "$f" > "$TMP/$n.s" 2> "$TMP/err" || { ok=0; note="$note $level: no code;"; continue; }
        # SPIM prints a 5-line banner before the program's own output
        timeout 60 spim -file "$TMP/$n.s" $args < "$in" > "$TMP/raw" 2> "$TMP/spimerr"; code=$?
        tail -n +6 "$TMP/raw" > "$TMP/out"; echo "exit: $code" >> "$TMP/out"
        if ! cmp -s "$TMP/out" "$T/expected/$n.out"; then
            ok=0; note="$note $level differs;"
            [ -z "$shown" ] && { diff "$TMP/out" "$T/expected/$n.out" | head -6 > "$TMP/diff.$n"; }
        fi
    done
    if [ $ok = 1 ]; then pass=$((pass + 1)); echo "  PASS  $n"
    else fail=$((fail + 1)); echo "  FAIL  $n  ($note )"; cat "$TMP/diff.$n" 2>/dev/null; fi
done
echo; echo "passed: $pass   failed: $fail"
[ "$fail" -eq 0 ]
