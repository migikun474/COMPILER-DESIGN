/* valid: parenthesized declarators read inside-out (regression: these
   were once mis-typed as arrays of pointers / wrong return types) */
int add(int a, int b) { return a + b; }
int *first(int *p) { return p; }
typedef int Vec[3];
typedef int (*Row)[3];            /* a typedef of a pointer to an array */
struct Ops { int (*grid)[3]; int data[2]; };

int main() {
    int a[3] = {1, 2, 3};
    int (*pa)[3] = &a;            /* pointer to an array of 3 int */
    int *ap[3];                   /* array of 3 pointers to int */
    ap[0] = &a[0];
    int (**ppa)[3] = &pa;         /* pointer to pointer to an array */
    int (*rows[2])[3];            /* array of 2 pointers to arrays */
    rows[0] = &a;
    rows[1] = *ppa;
    Row row = rows[0];
    Vec v = {4, 5, 6};
    struct Ops ops = {&a, {7, 8}};
    struct Ops many[2] = {{&a, {1, 2}}, {pa, {3, 4}}};
    int r = (*pa)[1] + *ap[0] + *first(a) + (**ppa)[2] + (*rows[1])[0] + (*row)[1] + add(5, 6);
    r = r + v[2] + (*ops.grid)[1] + ops.data[1] + many[1].data[0];
    return r;
}
