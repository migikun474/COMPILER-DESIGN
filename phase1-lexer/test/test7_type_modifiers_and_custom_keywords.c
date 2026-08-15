/* Covers:
 *  - size/sign type modifiers: short, long, long long, signed, unsigned
 *  - this language's custom reserved keywords that real C treats as
 *    ordinary library identifiers: printf, scanf, malloc, free, calloc,
 *    realloc
 */

int main() {
    short s = 5;
    long l = 100000;
    long long ll = 10000000000;
    signed int si = -3;
    unsigned int ui = 3;
    unsigned long ul = 4000000000;

    int *heap = (int *) malloc(10 * sizeof(int));
    int *more = (int *) calloc(5, sizeof(int));
    more = (int *) realloc(more, 10 * sizeof(int));
    heap[0] = 42;
    free(heap);
    free(more);

    printf("%d %d\n", si, ui);
    scanf("%d", &si);

    return 0;
}
