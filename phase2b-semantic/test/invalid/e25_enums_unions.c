/* invalid: what enums (C++ rules) and plain unions do not allow (D42) */
enum Color { Red, Green, Blue };
enum Size { Small, Large };
union U { int i; float f; };
struct S { int x; };
class K { public: int v; K() { v = 1; } };
union V { int i; int get() { return i; } };     // error: union 'V' cannot have member functions
union W { K k; int j; };                        // error: member 'k' of union 'W' has a class type with a constructor
union X { int &r; };                            // error: member 'r' of union 'X' cannot be a reference
enum Color { Again };                           // error: redefinition of 'enum Color'
struct U *pu;                                   // error: use of 'U' with tag type 'struct' that does not match its declaration as 'union'
enum Dup { Red };                               // error: redefinition of 'Red' (previously declared as an enumerator
enum { Big = 3000000000 };                      // error: does not fit the enum's underlying type 'int'
struct Holder { union { int a; float b; }; };   // error: anonymous unions are not supported
struct Outer { enum Inner { A, B } in; };       // error: an enum cannot be defined inside 'Outer'
int pick(int x) { return x; }

int main() {
    enum Color c = 1;                           // error: a value converts to an enum type only with a cast
    Color d = Small;                            // error: different enum types do not convert to each other
    c = c + 1;                                  // error: cannot assign 'int' to 'enum Color'
    c++;                                        // error: cannot increment a value of type 'enum Color'
    Red = 4;                                    // error: lvalue required
    union U u = { 1, 2.0f };                    // error: excess elements in union initializer
    enum Nope e;                                // error: use of undeclared enum 'enum Nope'
    enum S s2;                                  // error: 'S' is not an enum
    return pick(c) + u.i + d;
}
