/* valid: arithmetic, relational, logical, bitwise, assignment and unary
   operators with their implicit conversions [test 4, test 6] */
int main() {
    int a = 7, b = 2, r;
    double d = 3.0;
    char ch = 'a';
    unsigned int u = 5;

    r = a + b; r = a - b; r = a * b; r = a / b; r = a % b;
    d = a / d;                    /* int / double -> double */
    d = ch + 1.5;                 /* char -> double */
    r = ch;                       /* char -> int */
    ch = r;                       /* int -> char (narrowing is allowed in C) */
    r = (a < b) + (a <= b) + (a > b) + (a >= b) + (a == b) + (a != b);
    r = (a && b) || !a;
    r = (a & b) | (a ^ b) | ~a | (a << 2) | (a >> 1);
    a += b; a -= b; a *= b; a /= b; a %= b;
    a <<= 1; a >>= 1; a &= 3; a |= 4; a ^= 1;
    d += 2; d *= a;
    r = a++ + ++a - b-- - --b;      // warning: operation on 'a' may be undefined  // warning: operation on 'b' may be undefined
    r = -a + +b;
    r = a > b ? a : b;
    d = a > b ? a : d;            /* int and double arms -> double */
    r = (a = 3, b = 4, a + b);
    r = (int) d + (int) 'x';
    u = u + a;
    r = sizeof(int) + sizeof d + sizeof(char *);
    r = 1 ? 2 : 3;
    bool flag = a;                /* int -> bool */
    flag = d;
    return r + flag;
}
