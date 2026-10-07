/* valid: subtle name resolution and overload ranking */
int g(int *p) { return 1; }
int g(const int *p) { return 2; }   /* overload on pointee constness */
int f(int a);
int f(const int a) { return a; }    /* top-level const is not part of the signature */
static int helper(int a);

class A {
public:
    int x;
    int get() { return x; }
    int get(int k) { return x + k; }
    int twice() { return get() + get(2) + later(); }   /* `later` is declared below in the class */
    int fact(int n) { return n <= 1 ? 1 : n * fact(n - 1); }
    int later() { return 1; }
};

int main() {
    int x = 0;
    const int cx = 1;
    int r = g(&x) + g(&cx) + f(2);  /* g(int *) then g(const int *) */
    int proto(int);                 /* block-scope prototype of a file-scope function */
    r = r + proto(2) + helper(1);
    A obj;
    r = r + obj.twice() + obj.fact(4);
    {
        int r = 5;                  /* shadows the outer r inside this block only */
        x = r;
    }
    return r + x;
}
int proto(int a) { return a; }
static int helper(int a) { return a * 2; }
