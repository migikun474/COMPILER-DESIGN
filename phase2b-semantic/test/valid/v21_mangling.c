/* Name mangling (Itanium C++ ABI). Every `// mangled:` name is what g++
   emits for the same declaration (checked with g++ -c + nm); the test
   runner requires exactly these link names in both the parser's and the
   semantic symbol table. */
#include <stdio.h>
#include <stdarg.h>

struct Point { int x; int y; };

class Dog {
public:
    int age;
    Dog() { age = 0; }                                    // mangled: _ZN3DogC1Ev
    Dog(int a) { age = a; }                               // mangled: _ZN3DogC1Ei
    Dog(const Dog &o) { age = o.age; }                    // mangled: _ZN3DogC1ERKS_
    ~Dog() { }                                            // mangled: _ZN3DogD1Ev
    void bark() { }                                       // mangled: _ZN3Dog4barkEv
    static int count(int n) { return n; }                 // mangled: _ZN3Dog5countEi
    Dog &operator=(const Dog &o) { age = o.age; return *this; } // mangled: _ZN3DogaSERKS_
    int operator[](int i) { return i; }                   // mangled: _ZN3DogixEi
    bool operator==(const Dog &o) { return age == o.age; } // mangled: _ZN3DogeqERKS_
    int operator()(int a, int b) { return a + b; }        // mangled: _ZN3DogclEii
};

class Cat {
public:
    Cat(struct Point p);
    void meow(Cat *other, struct Point *where);
};
Cat::Cat(struct Point p) { }                              // mangled: _ZN3CatC1E5Point
void Cat::meow(Cat *other, struct Point *where) { }       // mangled: _ZN3Cat4meowEPS_P5Point

typedef unsigned int uint;
typedef struct Point Pt;
typedef int *IntPtr;

/* builtin types */
void f0() { }                                             // mangled: _Z2f0v
void f1(int a) { }                                        // mangled: _Z2f1i
void f2(char a, short b, long c, long long d) { }         // mangled: _Z2f2cslx
void f3(unsigned a, unsigned char b, unsigned short c, unsigned long d, unsigned long long e) { } // mangled: _Z2f3jhtmy
void f4(float a, double b, bool c) { }                    // mangled: _Z2f4fdb
/* pointers, const, substitutions; top-level const is not part of the signature */
void f5(int *a, int **b, const int *c, int *const d, const char *e, const char *f) { } // mangled: _Z2f5PiPS_PKiS_PKcS4_
void f6(struct Point a, struct Point *b, struct Point &c, const struct Point &d) { } // mangled: _Z2f65PointPS_RS_RKS_
void f8(Dog a, Dog *b, Dog &c) { }                        // mangled: _Z2f83DogPS_RS_
/* typedefs mangle as what they name */
void f9(uint a, Pt b) { }                                 // mangled: _Z2f9j5Point
void f25(IntPtr a, IntPtr b) { }                          // mangled: _Z3f25PiS_
/* decayed arrays, pointer to array */
void f12(int a[], char *argv[]) { }                       // mangled: _Z3f12PiPPc
void f13(int (*p)[3]) { }                                 // mangled: _Z3f13PA3_i
void f26(int a[][4]) { }                                  // mangled: _Z3f26PA4_i
/* variadic, references, void pointers */
void f14(const char *fmt, ...) { }                        // mangled: _Z3f14PKcz
void f17(int &a, int &b) { }                              // mangled: _Z3f17RiS_
void f18(struct Point *a, struct Point *b, struct Point c) { } // mangled: _Z3f18P5PointS0_S_
void f19(const struct Point *a, const struct Point *b) { } // mangled: _Z3f19PK5PointS1_
void f24(void *a, const void *b) { }                      // mangled: _Z3f24PvPKv
/* overloads and a free operator */
struct Point operator+(struct Point a, struct Point b) { return a; } // mangled: _Zpl5PointS_
int over(int a) { return a; }                             // mangled: _Z4overi
int over(double a) { return 0; }                          // mangled: _Z4overd
int over(struct Point *p) { return 0; }                   // mangled: _Z4overP5Point

int main() {                                              // mangled: main
    Dog d(3);
    Dog z;
    Dog e = d;
    e = d;
    d.bark();
    struct Point p;
    p.x = 1; p.y = 2;
    Cat c(p);
    c.meow(&c, &p);
    return over(1) + over(2.0) + Dog::count(e[1]) + d(1, 2) + (d == e);
}
