/* invalid: constructors, operator overloading, varargs, new declarators,
   designated initializers */
typedef int T;
typedef char T;                   // error: typedef redefinition with different types ('char' vs 'int')
struct S { int a; };
struct S { int b; };              // error: redefinition of 'struct S'
class Vec {
public:
    int x;
    Vec(int a) { x = a; }
    Vec operator+(Vec o, Vec p);  // error: must be a unary or binary operator (it has 3 operands)
    int operator!(int k);         // error: overloaded 'operator!' must be a unary operator
private:
    Vec(char *s);
};
int operator+(int a, int b);      // error: must have at least one parameter of class type
Vec operator=(Vec a, Vec b);      // error: overloaded 'operator=' must be a non-static member function
Vec::Vec(double d) { x = 0; }     // error: out-of-line definition of constructor 'Vec::Vec(double)' does not match
Vec::~Vec() { }                   // error: but 'class Vec' declares no destructor
int fixed(int n) { va_list ap; va_start(ap, n); return 0; }   // error: 'va_start' used in function 'fixed', which has fixed arguments
int var(int n, ...) {
    va_list ap;
    int k = 0;
    va_start(k, n);               // error: argument 1 of 'va_start' must be a 'va_list' variable
    char c = va_arg(ap, char);    // warning: 'char' is promoted to 'int' when passed through '...'
    int z = va_arg(ap, 3);        // error: second argument of 'va_arg' must be a type
    va_end(ap);
    return c + z;
}
int main() {
    Vec a;                        // error: 'class Vec' has no default constructor
    Vec b(1, 2);                  // error: no matching function for call to 'Vec::Vec(int, int)'
    Vec c("str");                 // error: 'Vec::Vec(char *)' is a private member of 'class Vec'
    Vec d = c * 2;                // error: no 'operator*' is declared for these operands
    c += d;                       // error: no 'operator+=' is declared
    int x = 1;
    int *const cp = &x;
    cp = 0;                       // error: cannot assign to variable 'cp' with const-qualified type 'int * const'
    int &*bad;                    // error: 'bad' declared as a pointer to a reference
    struct S s = {.nope = 1};     // error: no member named 'nope' in 'struct S'
    int arr[2] = {[5] = 1};       // error: array index 5 in initializer exceeds the bounds
    int k = {.a = 1};             // error: designator '.a' cannot be used to initialize the scalar
    int *p = new int[2.5];        // error: array size in 'new' must have an integer type, not 'double'
    delete[] x;                   // error: cannot delete[] an expression of type 'int'
    int q(1, 2);                  // error: is initialized with exactly one value, not 2
    int empty[] = {};             // error: zero-size array 'empty'
    int notConst[3] = {[x] = 1};  // error: array designator index must be an integer constant expression
    int below[3] = {[-1] = 1};    // error: array designator index -1 is negative
    int sz = sizeof(int) * 2;     /* (sizeof(int)) * 2, not sizeof((int) *2) */
    return 0;
}
