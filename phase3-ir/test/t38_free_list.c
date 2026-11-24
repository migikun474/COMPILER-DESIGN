/* t38 -- the heap reuses freed memory (D45): a freed block comes back from
   the next malloc of the same size, a long malloc/free loop runs in constant
   space, a list is freed and rebuilt, calloc clears a reused (dirty) block,
   realloc grows and shrinks keeping the contents, free(0) does nothing.
   Expected output: g++. */
struct Node { int value; struct Node *next; };

struct Node *build(int n) {
    struct Node *head = 0;
    int i;
    for (i = 1; i <= n; i++) {
        struct Node *p = (struct Node *)malloc(sizeof(struct Node));
        p->value = i;
        p->next = head;
        head = p;
    }
    return head;
}
int total(struct Node *p) { int s = 0; while (p) { s += p->value; p = p->next; } return s; }
void release(struct Node *p) { while (p) { struct Node *n = p->next; free(p); p = n; } }

int main() {
    char *a = (char *)malloc(1000);
    a[0] = 'x';
    free(a);
    char *b = (char *)malloc(1000);
    printf("reused %d\n", a == b);
    free(b);

    long long sum = 0;
    int i, k;
    for (i = 0; i < 50000; i++) {                 /* about 15 MB if nothing were reused */
        int *p = (int *)malloc(300);
        p[0] = i;
        p[74] = i * 2;
        sum += p[0] + p[74];
        free(p);
    }
    printf("loop %lld\n", sum);

    struct Node *list = build(100);
    printf("list %d\n", total(list));
    release(list);
    list = build(200);
    printf("list %d\n", total(list));
    release(list);

    int *dirty = (int *)malloc(64);
    for (k = 0; k < 16; k++) dirty[k] = 99;
    free(dirty);
    int *clean = (int *)calloc(16, sizeof(int));
    int nonzero = 0;
    for (k = 0; k < 16; k++) if (clean[k] != 0) nonzero++;
    printf("calloc %d\n", nonzero);
    free(clean);

    int *grow = (int *)malloc(4 * sizeof(int));
    int n = 4;
    for (k = 0; k < 4; k++) grow[k] = k;
    while (n < 64) {
        grow = (int *)realloc(grow, 2 * n * sizeof(int));
        for (k = n; k < 2 * n; k++) grow[k] = k;
        n = 2 * n;
    }
    int gsum = 0;
    for (k = 0; k < n; k++) gsum += grow[k];
    grow = (int *)realloc(grow, 8 * sizeof(int));
    printf("realloc %d %d %d\n", n, gsum, grow[7]);
    free(grow);
    free(0);
    return 0;
}
