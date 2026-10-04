/* invalid: semantic errors inside macro expansions are reported at the
   line as written (the diagnostic adds a note with the original text) */
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define CALL(f) f(1, 2, 3)
int add(int a, int b) { return a + b; }
int main() {
    char *bad = MAX(1, 2);      // error: cannot initialize variable 'bad' of type 'char *' with a value of type 'int'
    int r = CALL(add);          // error: function 'add' expects 2 arguments but 3 were provided
    return r;
}
