/* valid: parenthesized declarators read inside-out (regression: these
   were once mis-typed as arrays of pointers / wrong return types) */
int add(int a, int b) { return a + b; }
int *first(int *p) { return p; }
typedef int (*BinOp)(int, int);
typedef int Vec[3];
struct Ops { int (*fn)(int, int); int data[2]; };

int main() {
    int a[3] = {1, 2, 3};
    int (*pa)[3] = &a;            /* pointer to an array of 3 int */
    int *ap[3];                   /* array of 3 pointers to int */
    ap[0] = &a[0];
    int *(*pick)(int *q) = first; /* pointer to function returning int * */
    int (*one)(int, int) = add;
    int (**handle)(int, int) = &one;   /* pointer to pointer to function */
    int (*table[2])(int, int);    /* array of function pointers */
    table[0] = add;
    table[1] = *handle;
    BinOp op = table[0];
    Vec v = {4, 5, 6};
    struct Ops ops = {add, {7, 8}};
    struct Ops many[2] = {{add, {1, 2}}, {add, {3, 4}}};
    int r = (*pa)[1] + *ap[0] + *pick(a) + (*handle)(1, 2) + table[1](3, 4) + op(5, 6);
    r = r + v[2] + ops.fn(1, 1) + ops.data[1] + many[1].data[0];
    return r;
}
