/* valid: pointers, multi-level pointers, pointer arithmetic, void *,
   null [test 19, 20, 22] */
int add(int a, int b) { return a + b; }
int mul(int a, int b) { return a * b; }

void swap(int *a, int *b) {
    int t = *a;
    *a = *b;
    *b = t;
}

int main() {
    int x = 5, y = 6;
    int *p = &x;
    int **pp = &p;
    int ***ppp = &pp;
    int v = *p + **pp + ***ppp;
    **pp = 9;
    swap(&x, &y);
    int arr[4];
    int *q = arr + 2;             /* pointer + int */
    q = q - 1;
    int gap = q - arr;            /* pointer - pointer -> int */
    q++;
    --q;
    int same = (p == q) || (p != 0) || (q < arr + 4);
    p = 0;                        /* null pointer constant */
    void *raw = &x;               /* any object pointer -> void * */
    int *back = raw;              /* void * -> object pointer (C) */
    char *bytes = (char *) back;  /* explicit cast between pointer types */
    const int *ro = &x;           /* adding const is fine */
    v = v + add(2, 3) + mul(4, 5);
    if (p) v++;
    if (!q) v--;
    return v + gap + same + *ro + *bytes;
}
