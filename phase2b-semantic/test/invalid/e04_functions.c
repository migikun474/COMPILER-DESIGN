/* invalid functions and calls [tests 12, 13, 14, 15, 35] */
int add(int a, int b) { return a + b; }
void sink(int *p) { }
int takes_ptr(int *p) { return *p; }
double half(double v) { return v / 2; }

int proto(int a);
char proto(int a);                // error: conflicting types for 'proto'
int defined_twice(int a) { return a; }
int defined_twice(int a) { return a + 1; }   // error: redefinition of function 'defined_twice(int)'
int dup_params(int a, int a) { return a; }   // error: redefinition of parameter 'a'
void bad_param(void x) { }        // error: parameter 'x' cannot have type 'void'

int no_value() {
    return;                       // error: non-void function 'no_value' should return a value
}
void has_value() {
    return 10;                    // error: void function 'has_value' should not return a value
}
int wrong_type() {
    return "text";                // error: cannot return 'char *' from function 'wrong_type' whose return type is 'int'
}
int *wrong_ptr() {
    double d = 1;
    return d;                     // error: cannot return 'double'
}

int overloaded(int a) { return a; }
int overloaded(char *s) { return 0; }
int amb(int a, int b) { return 1; }
int amb(char a, char b) { return 2; }

int main() {
    int x = 1;
    char c = 'c';
    double d = 2.0;
    x = add(1);                   // error: function 'add' expects 2 arguments but 1 was provided
    x = add(1, 2, 3);             // error: function 'add' expects 2 arguments but 3 were provided
    x = add(&x, 2);               // error: argument 1 of 'add' expects 'int' but got 'int *'
    x = takes_ptr(c);             // error: argument 1 of 'takes_ptr' expects 'int *' but got 'char'
    sink(d);                      // error: argument 1 of 'sink' expects 'int *' but got 'double'
    x = x(3);                     // error: called object of type 'int' is not a function
    x = missing(1);               // error: call to undeclared function 'missing'
    x = overloaded(d);            /* double -> int is a standard conversion: picks overloaded(int) */
    x = overloaded(&d);           // error: no matching function for call to 'overloaded(double *)'
    x = amb(c, 2);                // error: call to overloaded function 'amb(char, int)' is ambiguous
    x = half;                     // error: cannot assign 'double (*)(double)' to 'int'
    x = sink(&x);                 // error: a void expression has no value
    return x;
}
