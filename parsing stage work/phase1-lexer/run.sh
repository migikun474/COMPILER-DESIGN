#!/bin/bash
# Usage: ./run.sh [path-to-executable]
# Runs the given lexer executable (defaults to ./lexer) over every .c file
# in the test/ directory and prints the result for each.

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
EXEC="${1:-$SCRIPT_DIR/lexer}"
TEST_DIR="$SCRIPT_DIR/test"

if [ ! -x "$EXEC" ]; then
    echo "Error: executable '$EXEC' not found or not executable. Build it first with 'make'."
    exit 1
fi

for f in "$TEST_DIR"/*.c; do
    echo "===================================================================="
    echo "Test file: $(basename "$f")"
    echo "===================================================================="
    "$EXEC" "$f"
    echo
done
