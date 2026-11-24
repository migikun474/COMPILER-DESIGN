/* t05 -- pointers: two and three levels, arithmetic and differences,
   void * round trips, a pointer to an array, an array of pointers,
   comparison, writing through a pointer to a pointer. Expected: g++. */
void redirect(int **pp, int *to) { *pp = to; }
int main() {
    int x = 3, y = 9;
    int *p = &x, **pp = &p, ***ppp = &pp;
    ***ppp = 4;
    redirect(pp, &y);
    printf("%d %d %d\n", x, *p, **pp);
    int a[5] = {10, 20, 30, 40, 50};
    int *q = a + 1, *r = &a[4];
    printf("%d %d %d %d\n", *q, *(q + 2), (int)(r - q), r > q);
    q += 2;
    *q-- = 7;
    printf("%d %d\n", a[3], *q);
    void *v = &a[2];
    int *back = (int *)v;
    printf("%d\n", *back);
    int row[3] = {1, 2, 3};
    int (*pa)[3] = &row;
    printf("%d %d\n", (*pa)[2], (int)sizeof(*pa));
    int *list[3] = {&x, &y, &a[0]};
    int s = 0, i;
    for (i = 0; i < 3; i++) s += *list[i];
    printf("%d\n", s);
    return 0;
}
