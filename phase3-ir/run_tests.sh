#!/bin/bash
# Usage: ./run_tests.sh [--update]
#
# Runs every test/*.c through the TAC generator and the TAC interpreter
# and compares what the program prints, and its exit code, with
# test/expected/<name>.out. Those files were checked against g++/gcc
# compiling the same sources. test/<name>.in is the program's input,
# test/<name>.args its command-line arguments. A test with an
# expected/<name>.tac file must also produce exactly that listing.
# Every program is then run again with -O1, -O2 and -O3 and must behave
# identically; the line shows the instructions executed without
# optimization and how many fewer each level executes.
#
# --update rewrites the expected files from the current build.

cd "$(dirname "${BASH_SOURCE[0]}")" || exit 1
[ -x ./tac_generator ] || { echo "Build it first with 'make'."; exit 1; }
TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
pass=0; fail=0
for f in test/*.c; do
    n="$(basename "$f" .c)"
    args=""; [ -f "test/$n.args" ] && args="$(cat "test/$n.args")"
    in=/dev/null; [ -f "test/$n.in" ] && in="$PWD/test/$n.in"
    (cd "$TMP" && "$OLDPWD/tac_generator" --run -q "$OLDPWD/$f" $args < "$in" > out 2> err; echo "exit: $?" >> out
     "$OLDPWD/tac_generator" "$OLDPWD/$f" 2>/dev/null | sed '1,2d' > tac)
    if [ "$1" = "--update" ]; then
        cp "$TMP/out" "test/expected/$n.out"
        [ -f "test/expected/$n.tac" ] && cp "$TMP/tac" "test/expected/$n.tac"
    fi
    # the same program optimized: it must print and return exactly the same
    ok=1
    gain=""
    for level in 1 2 3; do
        (cd "$TMP" && "$OLDPWD/tac_generator" -O$level --run -q "$OLDPWD/$f" $args < "$in" > out1 2> err1; echo "exit: $?" >> out1)
        cmp -s "$TMP/out1" "test/expected/$n.out" || ok=0
        gain="$gain  -O$level $(grep -o '[0-9]*% fewer' "$TMP/err1")"
    done
    raw="$(grep -o '[0-9]* instructions executed' "$TMP/err" | grep -o '[0-9]*')"
    cmp -s "$TMP/out" "test/expected/$n.out" || ok=0
    [ -f "test/expected/$n.tac" ] && { cmp -s "$TMP/tac" "test/expected/$n.tac" || ok=0; }
    if [ $ok = 1 ]; then pass=$((pass + 1)); printf '  PASS  %-22s %6s executed %s\n' "$n" "$raw" "$gain"
    else fail=$((fail + 1)); echo "  FAIL  $n"; diff "$TMP/out" "test/expected/$n.out" | head -5; diff "$TMP/out1" "test/expected/$n.out" | head -5; fi
done
echo; echo "passed: $pass   failed: $fail"
[ "$fail" -eq 0 ]
