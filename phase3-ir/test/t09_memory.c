/* t09 -- the heap: malloc, calloc (zeroed even when reused), realloc
   keeping the contents, free giving memory back (the next malloc of that
   size reuses it), a linked list built, reversed and freed, a table of
   rows from malloc, a long malloc/free loop. Expected: g++. */
struct Node { int v; struct Node *next; };
struct Node *push(struct Node *h, int v) { struct Node *n = (struct Node *)malloc(sizeof(struct Node)); n->v = v; n->next = h; return n; }
int main() {
    struct Node *list = 0, *rev = 0;
    int i;
    for (i = 1; i <= 5; i++) list = push(list, i);
    while (list) { struct Node *n = list->next; list->next = rev; rev = list; list = n; }
    int s = 0;
    for (list = rev; list; list = list->next) s = s * 10 + list->v;
    printf("%d\n", s);
    while (rev) { struct Node *n = rev->next; free(rev); rev = n; }
    int **rows = (int **)malloc(3 * sizeof(int *));
    for (i = 0; i < 3; i++) { rows[i] = (int *)calloc(4, sizeof(int)); rows[i][i] = i + 1; }
    printf("%d %d %d\n", rows[2][2], rows[1][0], rows[0][0] + rows[1][1]);
    int *g = (int *)malloc(2 * sizeof(int));
    g[0] = 11; g[1] = 22;
    g = (int *)realloc(g, 50 * sizeof(int));
    g = (int *)realloc(g, 2 * sizeof(int));        /* shrinking: the same block */
    printf("%d %d\n", g[0], g[1]);
    char *a = (char *)malloc(100);
    free(a);
    char *b = (char *)malloc(100);
    printf("%d\n", a == b);
    long long total = 0;
    for (i = 0; i < 30000; i++) { int *t = (int *)malloc(400); t[99] = i; total += t[99]; free(t); }
    printf("%lld\n", total);
    return 0;
}
