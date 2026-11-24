/* t39 -- printf %p: "0x" and the address in lowercase hex,
   "(nil)" for a null pointer, the field width and '-' applied to the whole
   text -- glibc's format. Real addresses differ between machines, so the
   pointers here are made from fixed numbers, which print the same on g++,
   the TAC interpreter and SPIM. Expected output: g++. */
int main() {
    int *none = 0;
    int *small = (int *)0x10;
    char *mid = (char *)0x1234abcd;
    unsigned int big = 0xdeadbeef;
    double *top = (double *)big;
    void *one = (void *)1;
    printf("[%p] [%p] [%p] [%p] [%p]\n", none, small, mid, top, one);
    printf("[%12p] [%-12p] [%3p]\n", mid, mid, mid);
    printf("[%10p] [%-10p] [%2p]\n", none, none, none);
    printf("%p and %d and %p\n", small, 42, (void *)0xff);
    int *p = small + 2;                            /* pointer arithmetic: 0x10 + 2 * 4 */
    char *c = mid + 3;
    printf("%p %p %d\n", p, c, (int)(p - small));
    return 0;
}
