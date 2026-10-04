/* valid but suspicious: accepted with warnings (exit status 0) */
int helper(int v);                // warning: is used but never defined

int compute(int v) {              // warning: has no return statement
    v = v + 1;
}

int main() {
    int a[4];
    int x = 1;
    a[4] = 0;                     // warning: past the end of the array
    a[-1] = 0;                    // warning: before the beginning
    x = x / 0;                    // warning: division by zero
    printf("%d %d\n", x);         // warning: expects 2 arguments after the format, but 1 was provided
    printf("%s\n", x);            // warning: format '%s' expects a string
    int m = 'ab';                 // warning: multi-character character constant
    static y;                     // warning: type specifier missing, defaults to 'int'
    return helper(x) + compute(m) + y;
}
