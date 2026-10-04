#!/bin/bash
# Usage: ./run.sh [path-to-executable]
# Runs the given semantic analyzer executable (defaults to
# ./semantic_analyzer) over every .c file in test/valid and test/invalid
# and prints the result for each. For the self-checking version, which
# verifies every expected diagnostic, use ./run_tests.sh.

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
EXEC="${1:-$SCRIPT_DIR/semantic_analyzer}"

if [ ! -x "$EXEC" ]; then
    echo "Error: executable '$EXEC' not found or not executable. Build it first with 'make'."
    exit 1
fi

for f in "$SCRIPT_DIR"/test/valid/*.c "$SCRIPT_DIR"/test/invalid/*.c; do
    echo "===================================================================="
    echo "Test file: ${f#$SCRIPT_DIR/}"
    echo "===================================================================="
    "$EXEC" "$f"
    echo
done
