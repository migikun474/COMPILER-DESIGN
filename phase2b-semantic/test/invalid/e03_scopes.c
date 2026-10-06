/* invalid scope access [test 10]: a name exists somewhere, but is not
   visible at this point */
int use_before() {
    return later_global;          // error: it is declared later, at line 23
}

int main() {
    {
        int inner = 1;
    }
    inner = 2;                    // error: undeclared identifier 'inner'
    for (int i = 0; i < 3; i++) { }
    i = 5;                        // error: undeclared identifier 'i'
    if (1) {
        int deep = 3;
        { int deeper = deep; }
        deeper = 4;               // error: undeclared identifier 'deeper'
    }
    int self = self + 1;          /* legal C: `self` is in scope in its own initializer */
    return helper_local;          // error: undeclared identifier 'helper_local'
}

int later_global = 5;

int other() {
    int helper_local = 1;
    return helper_local;
}
