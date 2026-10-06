/* Unnamed aggregates: the same mistakes g++ reports, at the same lines. */
struct Dup { int i; struct { int i; float f; }; };   // error: duplicate member 'i' in struct 'Dup'
struct Dup2 { struct { int k; }; struct { char k; }; }; // error: duplicate member 'k' in struct 'Dup2'
class Box { struct { int secret; float fs; }; public: int open; };
typedef struct { int x; } Pt;
struct { int a; } g;
struct { int unused; };                               // warning: unnamed struct that defines no instances

int main() {
    Pt p;
    Box b;
    p.z = 1;                                          // error: no member named 'z' in 'Pt'
    p = 5;                                            // error: cannot assign 'int' to 'Pt'
    g.b = 2;                                          // error: no member named 'b' in 'struct (unnamed at 6:1)'
    int *ip = &p;                                     // error: of type 'int *' with a value of type 'Pt *'
    b.secret = 3;                                     // error: 'secret' is a private member of 'class Box'
    Pt q = { .x = 1, .w = 2 };                        // error: no member named 'w' in 'Pt'
    struct { int s1; };                               // warning: unnamed struct that defines no instances
    s1 = 4;                                           // error: undeclared identifier 's1'
    return q.x + *ip;
}
