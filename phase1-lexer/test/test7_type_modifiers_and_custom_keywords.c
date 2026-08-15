/* Covers:
 *  - size/sign type modifiers: short, long, long long, signed, unsigned
 *  - this language's custom reserved keywords that real C treats as
 *    ordinary library identifiers: printf, scanf, malloc, free, calloc,
 *    realloc
 *  - numeric literal forms: hex (0x1F), octal (017), binary (0b1101),
 *    integer suffixes (U, L, LL and their combinations), float suffix
 *    (f), and leading/trailing-dot floats (.5, 5.)
 *  - boolean literals: true, false
 */

int main() {
    short s = 5;
    long l = 100000;
    long long ll = 10000000000;
    signed int si = -3;
    unsigned int ui = 3;
    unsigned long ul = 4000000000;

    int hex = 0x1F;
    int oct = 017;
    int bin = 0b1101;
    unsigned int u1 = 45U;
    unsigned int u2 = 45u;
    long l1 = 45L;
    unsigned long ul1 = 45UL;
    long long ll1 = 45LL;
    unsigned long long ull1 = 45ULL;
    unsigned long long ull2 = 45LLU;
    float f = 3.14f;
    float leading_dot = .5;
    float trailing_dot = 5.;

    int flag_true = true;
    int flag_false = false;

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
