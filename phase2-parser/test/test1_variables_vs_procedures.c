/* Demonstrates the whole point of phase 2: an identifier's Token_Type
 * is resolved from *how it's declared/used*, not just "identifier".
 *
 *   - inside main(), `a` is declared as a plain int  -> classified INT
 *   - at file scope, `a` is declared as a function    -> classified PROCEDURE
 * (two different `a`s, in two different scopes -- exactly like real C)
 */

int a(int b, int c) {
    return b + c;
}

int main() {
    int a;
    a = 5;
    int result = a + 1;
    return 0;
}
