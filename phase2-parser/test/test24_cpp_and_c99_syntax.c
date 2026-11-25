/* test24 -- syntax added after phase 2 was first finished, so that the
   language's C++-style features can actually be *used*: default
   constructors defined out of class, `Class::member` in
   expressions, a class name used as a type inside its own body,
   operator overloading, const pointers and references
   to pointers, unnamed (abstract) parameters and pointer-to-array casts,
   designated and empty initializers, adjacent string literals, and a
   struct that is a type only inside its own block. A fully valid
   program. */
typedef int T;
class Node {
public:
    int value;
    Node *next;
    Node();
    static int count();
    Node operator+(Node o) { Node r; r.value = value + o.value; return r; }
    int get() { return this->value; }
};
Node::Node() { value = 1; next = 0; }
int Node::count() { return 1; }
struct Pt { int x; int y; };
int sum(int n, int m) {
    int s = n + m;
    return s;
}
int apply(int *, int);
int apply(int *f, int v) { return *f + v; }
int twice(int v) { return v * 2; }
int main() {
    Node a;
    Node b;
    b.next = &a;
    Node c = a + b;
    int *many = (int *) malloc(4 * sizeof(int));
    int x(5);
    int *const cp = &x;
    int *&rp = many;
    struct Pt p = {.y = 2, .x = 1};
    int arr[4] = {[1] = 7};
    int zeros[2] = {};
    char *s = "adj" "acent";
    int (*grid)[4] = (int (*)[4]) &arr;
    {
        struct Local { int k; };
    }
    int Local = 0;
    int T = 3;
    free(many);
    return Node::count() + sum(1, 2) + *cp + *rp + p.x + arr[1] +
           zeros[0] + s[0] + (*grid)[1] + apply(&x, 1) + twice(2) + Local + T + c.get();
}
