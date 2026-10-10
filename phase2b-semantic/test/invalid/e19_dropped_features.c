/* invalid: what is left of the dropped features once a program parses.
   Function pointers are gone, so a function is never a value: its name
   can only be called. (enum, union, FILE, lambdas and `int (*fp)(int)`
   are rejected earlier, as syntax errors: phase2-parser/test/
   test29_dropped_features.c, and so are `new`, `delete`, `register`
   and `volatile`, dropped later. `long double` is no longer a spelling
   of `double`.) */
typedef int Fn(int);
long double wide;                 // error: invalid combination of type specifiers 'long double'
int twice(int v) { return v * 2; }
int apply(int op(int), int v) { return v; }   // error: parameter 'op' cannot have a function type
Fn *handler;                      // error: 'handler' declared as a pointer to a function
Fn &alias;                        // error: 'alias' declared as a reference to a function
void sink(void *p) { }

class Shape {
public:
    int area() { return 1; }
    static int count() { return 0; }
    int bad() { return area; }    // error: reference to non-static member function 'area' must be called
    int bad2() { return count; }  // error: reference to static member function 'count' must be called
};

int main() {
    int x = 0;
    Shape s;
    x = twice;                    // error: reference to function 'twice' must be called
    int *q = &twice;              // error: reference to function 'twice' must be called
    x = *twice;                   // error: function pointers are not supported
    x = (*twice)(3);              // error: reference to function 'twice' must be called
    sink(twice);                  // error: reference to function 'twice' must be called
    if (twice) x = 1;             // error: reference to function 'twice' must be called
    x = twice ? 1 : 2;            // error: reference to function 'twice' must be called
    x = sizeof(twice);            // error: reference to function 'twice' must be called
    x = s.area;                   // error: reference to member function 'area' must be called
    x = x(3);                     // error: called object of type 'int' is not a function
    x = (twice)(3) + twice(4);    /* calling is the one thing a function name is for */
    return x + s.area() + Shape::count();
}
