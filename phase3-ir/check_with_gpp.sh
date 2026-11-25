#!/bin/bash
# Usage: ./check_with_gpp.sh
#
# Compiles every test/*.c with g++ (with gcc in C mode when g++ rejects
# it, as for t04's C designators) and checks that the native program
# prints and returns exactly test/expected/<name>.out -- the same file
# run_tests.sh compares the compiler against. test/gpp_prelude.h supplies
# the #includes and defines `until`, which the programs themselves cannot
# do (no preprocessor, D34). Inputs and arguments: test/<name>.in,
# test/<name>.args, as in run_tests.sh.

cd "$(dirname "${BASH_SOURCE[0]}")" || exit 1
TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
pass=0; fail=0
for f in test/*.c; do
    n="$(basename "$f" .c)"
    args=""; [ -f "test/$n.args" ] && args="$(cat "test/$n.args")"
    in=/dev/null; [ -f "test/$n.in" ] && in="$PWD/test/$n.in"
    how="g++"
    if ! g++ -w -x c++ -include test/gpp_prelude.h -o "$TMP/$n" "$f" 2> "$TMP/err"; then
        how="gcc"
        gcc -w -x c -include test/gpp_prelude.h -o "$TMP/$n" "$f" 2>> "$TMP/err" || {
            fail=$((fail + 1)); echo "  FAIL  $n (does not compile with g++ or gcc)"; head -3 "$TMP/err"; continue; }
    fi
    (cd "$TMP" && ./"$n" $args < "$in" > out 2>/dev/null; echo "exit: $?" >> out)
    if cmp -s "$TMP/out" "test/expected/$n.out"; then
        pass=$((pass + 1)); printf '  PASS  %-22s (%s)\n' "$n" "$how"
    else
        fail=$((fail + 1)); echo "  FAIL  $n ($how)"; diff "$TMP/out" "test/expected/$n.out" | head -5
    fi
done
echo
echo "passed: $pass   failed: $fail"
[ $fail = 0 ]
