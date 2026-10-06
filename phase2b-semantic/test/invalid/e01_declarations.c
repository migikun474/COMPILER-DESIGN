/* invalid declarations [test 2: duplicate declaration, test 3: undeclared variable] */
int g;
int g;                            // error: duplicate declaration of 'g' in the same scope
int f(int a) { return a; }
int f;                            // error: redefinition of 'f' as a different kind of symbol
typedef int T;
void nothing;                     // error: variable 'nothing' has incomplete type 'void'
struct Missing m;                 // error: has incomplete type 'struct Missing'
FILE handle;                      // error: incomplete type 'FILE' (declare a pointer
int unsized[];                    // error: needs an explicit size or an initializer
int counter = 0;
int twice = counter * 2;          // error: initializer element is not a compile-time constant

int main() {
    int x;
    int x;                        // error: duplicate declaration of 'x'
    char x;                       // error: duplicate declaration of 'x'
    y = 10;                       // error: undeclared identifier 'y'
    int z = w + 1;                // error: undeclared identifier 'w'
    auto a;                       // error: deduced type 'auto' requires an initializer
    int char bad;                 // error: invalid combination of type specifiers 'int char'
    unsigned signed both;         // error: invalid combination of type specifiers
    int &dangling;                // error: reference variable 'dangling' requires an initializer
    static int s = x;             // error: initializer element is not a compile-time constant
    return late;                  // error: it is declared later, at line
}

int late = 1;
