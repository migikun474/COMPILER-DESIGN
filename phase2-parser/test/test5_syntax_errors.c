/* Deliberately broken -- exercises error reporting/recovery. Expected:
 * the analyzer should report several distinct syntax errors (missing
 * semicolon, missing closing paren, empty initializer expression) and
 * print NO token table, instead of silently accepting the file or
 * stopping after the very first mistake. */

int main() {
    int a
    a = 5;

    if (a > 0 {
        printf("hi");
    }

    int b = ;
    return 0;
}
