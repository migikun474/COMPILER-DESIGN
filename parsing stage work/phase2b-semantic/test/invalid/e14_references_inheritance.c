/* invalid: references, multiple inheritance, protected access through a
   base pointer, const propagation through pointers */
class L { public: int v; int left() { return 1; } };
class R { public: int v; int right() { return 2; } };
class Both : public L, public R { public: int mine() { return left() + right(); } };
class Prot { protected: int p; };
class Kid : public Prot {
public:
    int ok(class Kid *k) { return k->p + p; }
    int bad(class Prot *o) { return o->p; }   // error: 'p' is a protected member of 'class Prot' and is not accessible from class 'Kid'
};
struct P { int x; };
int g = 0;
int &pick() { return g; }
int &bad_ref() { return 5; }      // error: non-const reference of type 'int &' cannot bind to a temporary of type 'int'
void bump(int &r) { r++; }
void show(const int &r) { }

int main() {
    Both b;
    int v = b.v;                  // error: member 'v' is found in more than one base class of 'Both'
    v = b.left() + b.mine();
    int x = 1;
    int &r = x;
    int *p = &r;                  /* the address of a reference is the referent's */
    r = 3;
    pick() = 7;                   /* a returned reference is an lvalue */
    bump(5);                      // error: argument 1 of 'bump' expects 'int &' but got 'int'
    bump(x);
    show(5);                      /* a const reference may bind to a temporary */
    const struct P cp = {1};
    struct P *pp = &cp;           // error: conversion discards 'const' qualifier
    const struct P *cpp = &cp;
    cpp->x = 3;                   // error: cannot assign to a read-only location of type 'const int'
    for (int i = 0, j = 10; i < j; i++, j--) { v += i * j; }
    printf("%d\n", cp);           // warning: format '%d' expects an integer, but argument 2 has type 'struct P'
    return v + *p;
}
