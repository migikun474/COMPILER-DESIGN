/* malloc/free/calloc/realloc and the fopen/fprintf/... family are
 * lexer keywords in this language (see phase1), not ordinary library
 * identifiers -- so they're parsed as builtin calls rather than as
 * IDENTIFIER function calls, and a cast like `(int *) malloc(...)`
 * needs the parser to accept a type-name (not just an expression)
 * inside parentheses right before a unary-expr. */

int main() {
    int *heap;
    heap = (int *) malloc(10 * 4);
    heap[0] = 42;
    free(heap);

    int *more;
    more = (int *) calloc(5, 4);
    more = (int *) realloc(more, 20);
    free(more);

    FILE *f;
    f = fopen("data.txt", "r");
    fprintf(f, "%d\n", 42);
    fclose(f);

    return 0;
}
