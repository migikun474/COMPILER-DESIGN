/* Anonymous unions outside a record (C++): `union { int a; char b; };`
   makes one hidden union object, and a, b are variables living in it,
   sharing its storage. At file scope it must be `static`. */

static union { int bits; float real; };       /* file scope */

int classify(int v) {
    union {                                    /* block scope */
        int word;
        char bytes[4];
        union { short half; char first; };     /* an anonymous union may nest */
    };
    word = v;
    if (bytes[0] == 0) return half;
    return first + word;
}

int counter() {
    static union { int calls; unsigned u; };  /* static storage, like any static local */
    calls = calls + 1;
    return calls;
}

int main() {
    bits = 0;
    real = 1.5f;
    int *p = &bits;                            /* an lvalue like any variable */
    int n = sizeof(real) + sizeof bits;
    for (int i = 0; i < 3; i++) {
        union { int k; float kf; };            /* a fresh one per block */
        k = i;
        n = n + k;
    }
    union { long total; char tag; };
    total = classify(n) + counter();
    tag = 'z';
    return *p + n + (int)total + tag;
}
