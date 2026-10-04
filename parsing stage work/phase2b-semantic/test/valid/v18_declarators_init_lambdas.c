/* valid: const pointers and references to pointers, unnamed parameters,
   designated and empty initializers, lambda extras, va_list, string
   concatenation, scoped type names */
typedef int T;
struct Pt { int x; int y; int z; };
struct Node { int v; struct Node *next; };

int sum(int n, ...) {
    va_list ap;
    va_start(ap, n);
    int s = 0;
    for (int i = 0; i < n; i++) s += va_arg(ap, int);
    double tail = va_arg(ap, double);
    va_end(ap);
    return s + tail;
}
int apply(int (*)(int), int);           /* unnamed function-pointer parameter */
int apply(int (*f)(int), int v) { return f(v); }
int twice(int v) { return v * 2; }

class Counter {
public:
    int count;
    int bump() { auto f = [this]() { count++; return count; }; return f(); }
};

int main() {
    int x = 1, y = 2;
    int *const cp = &x;                 /* the pointer is const, the int is not */
    *cp = 5;
    int *p2 = &y;
    int *&rp = p2;                      /* reference to a pointer */
    rp = &x;
    const int *pc = &x;                 /* the int is const, the pointer is not */
    pc = &y;
    auto counter = [x]() mutable { x = x + 1; return x; };
    auto typed = [](int v) -> double { return v / 2; };
    auto noParams = [&] { return x + y; };
    struct Pt p = {.y = 2, .x = 1};     /* designated */
    int arr[5] = {[2] = 7, 8};          /* arr[3] = 8 */
    int sized[] = {[4] = 1};            /* 5 elements */
    int zeros[3] = {};
    struct Pt origin = {};
    int scalar = {};
    char *word = "adj" "acent";
    int (*fn)(int) = (int (*)(int)) twice;
    int T = 3;                          /* a local variable hides the typedef T */
    {
        struct Local { int k; };
        struct Local l = {1};
        x += l.k;
    }
    int Local = 4;                      /* struct Local's name ended with its block */
    Counter c;
    struct Node n1;
    n1.next = 0;
    return apply(twice, 3) + typed(4) + noParams() + counter() + p.x + arr[3] + sized[4] + zeros[0] +
           origin.z + scalar + word[0] + fn(1) + T + Local + *pc + c.bump() + sum(2, 1, 2, 3.0);
}
