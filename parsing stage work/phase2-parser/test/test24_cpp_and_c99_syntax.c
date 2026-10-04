/* test24 -- syntax added after phase 2 was first finished, so that the
   language's C++-style features can actually be *used*: constructor
   calls, out-of-class constructors/destructors, `Class::member` in
   expressions, a class name used as a type inside its own body,
   operator overloading, `new T(args)` / `new T[n]` / `delete[]`,
   va_list / va_start / va_arg / va_end, `mutable` / `-> T` / `[this]` /
   parameter-less lambdas, const pointers and references to pointers,
   unnamed (abstract) parameters and function-pointer casts, designated
   and empty initializers, adjacent string literals, and a struct that is
   a type only inside its own block. A fully valid program. */
typedef int T;
class Node {
public:
    int value;
    Node *next;
    Node(int v);
    Node(int v, Node *n) { value = v; next = n; }
    ~Node();
    static int count();
    Node operator+(Node o) { return Node(value + o.value); }
    int get() { auto f = [this]() { return value; }; return f(); }
};
Node::Node(int v) { value = v; next = 0; }
Node::~Node() { }
int Node::count() { return 1; }
struct Pt { int x; int y; };
int sum(int n, ...) {
    va_list ap;
    va_start(ap, n);
    int s = va_arg(ap, int);
    va_end(ap);
    return s;
}
int apply(int (*)(int), int);
int apply(int (*f)(int), int v) { return f(v); }
int twice(int v) { return v * 2; }
int main() {
    Node a(1);
    Node b(2, &a);
    Node c = a + b;
    Node *heap = new Node(3);
    int *many = new int[4];
    int x(5);
    int *const cp = &x;
    int *&rp = many;
    auto counter = [x]() mutable { x++; return x; };
    auto typed = [](int v) -> double { return v; };
    auto bare = [&] { return x; };
    struct Pt p = {.y = 2, .x = 1};
    int arr[4] = {[1] = 7};
    int zeros[2] = {};
    char *s = "adj" "acent";
    int (*fn)(int) = (int (*)(int)) twice;
    {
        struct Local { int k; };
    }
    int Local = 0;
    int T = 3;
    delete heap;
    delete[] many;
    return Node::count() + sum(1, 2) + *cp + *rp + counter() + typed(1) + bare() + p.x + arr[1] +
           zeros[0] + s[0] + fn(1) + apply(twice, 1) + Local + T + c.get();
}
