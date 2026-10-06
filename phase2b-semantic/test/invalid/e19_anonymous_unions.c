/* Anonymous unions outside a record: the rules g++ enforces, at the
   lines g++ reports them. */
union { int g1; float g2; };                   // error: anonymous union at file scope must be declared 'static'
static union { int s1; float s2; };

int main() {
    int x = 0;
    union { int a; char b; };
    union { int x; };                          // error: duplicate declaration of 'x' in the same scope
    union { int m; void f(); };                // error: member function 'f()' is not allowed in an anonymous union
    union { private: int p; };                 // error: private member 'p' is not allowed in an anonymous union
    union { struct { int lo, hi; }; int w; };  // error: an anonymous struct is only allowed inside a named
    union { int a; };                          // error: duplicate declaration of 'a' in the same scope
    a = 1;
    b = 'c';
    s1 = 2;
    a = "text";                                // error: cannot assign
    return a + s1 + g1;                        // error: undeclared identifier 'g1'
}
