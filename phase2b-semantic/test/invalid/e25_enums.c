/* invalid: what enums (C++ rules) do not allow (D42) */
enum Color { Red, Green, Blue };
enum Size { Small, Large };
struct S { int x; };
enum Color { Again };                           // error: redefinition of 'enum Color'
enum Dup { Red };                               // error: redefinition of 'Red' (previously declared as an enumerator
enum { Big = 3000000000 };                      // error: does not fit the enum's underlying type 'int'
struct Outer { enum Inner { A, B } in; };       // error: an enum cannot be defined inside 'Outer'
int pick(int x) { return x; }

int main() {
    enum Color c = 1;                           // error: a value converts to an enum type only with a cast
    Color d = Small;                            // error: different enum types do not convert to each other
    c = c + 1;                                  // error: cannot assign 'int' to 'enum Color'
    c++;                                        // error: cannot increment a value of type 'enum Color'
    Red = 4;                                    // error: lvalue required
    enum Nope e;                                // error: use of undeclared enum 'enum Nope'
    enum S s2;                                  // error: 'S' is not an enum
    return pick(c) + d;
}
