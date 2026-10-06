/* invalid types in expressions and assignments
   [test 5: incompatible assignment, test 7: invalid operand types] */
struct P { int x; };

int main() {
    int i = 1, *p = &i;
    char c = 'c';
    double d = 1.0;
    struct P s, t;
    const int k = 3;
    const int *ro = &i;
    int *q;

    p = c;                        // error: cannot assign 'char' to 'int *'
    i = p;                        // error: cannot assign 'int *' to 'int'
    int *bad = 5;                 // error: cannot initialize variable 'bad' of type 'int *' with a value of type 'int'
    char *str = d;                // error: with a value of type 'double'
    s = 5;                        // error: cannot assign 'int' to 'struct P'
    i = s;                        // error: cannot assign 'struct P' to 'int'
    i = s + 1;                    // error: invalid operands to binary '+'
    d = d % 2;                    // error: both operands of '%' must be integers
    i = p * 2;                    // error: invalid operands to binary '*'
    q = p + p;                    // error: two pointers cannot be added
    i = d << 1;                   // error: both operands of a shift must be integers
    i = ~d;                       // error: to unary '~'
    i = -s;                       // error: to unary '-'
    i = s && 1;                   // error: invalid operands to binary '&&' ('struct P' and 'int')
    i = (p == c + 1);             // error: comparison between pointer and integer
    k = 4;                        // error: cannot assign to variable 'k' with const-qualified type 'const int'
    *ro = 5;                      // error: cannot assign to a read-only location of type 'const int'
    q = ro;                       // error: discards 'const' qualifier
    5 = i;                        // error: lvalue required as left operand of assignment
    i++ = 3;                      // error: lvalue required as left operand of assignment
    ++5;                          // error: lvalue required as increment operand
    (i = 1) = 2;                  // error: lvalue required
    i = (struct P) 3;             // error: invalid cast from 'int' to 'struct P'
    i = (int) s;                  // error: invalid cast from 'struct P' to 'int'
    i = (d > 0) ? p : d;          // error: incompatible operand types in conditional expression
    p += d;                       // error: invalid operands to compound assignment '+='
    i = 1 + 1 ? s : i;            // error: incompatible operand types
    return i;
}
