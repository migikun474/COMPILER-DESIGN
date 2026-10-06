/* invalid arrays [test 18] */
int n = 4;
int vla[n];                       // error: array size must be an integer constant expression
int zero[0];                      // error: array size must be greater than zero
int negative[-2];                 // error: array size must be greater than zero ('-2' given)
int fractional[2.5];              // error: array size must be an integer constant expression
int bad_dims[][];                 // error: only the first dimension of array 'bad_dims' may be left unspecified
int too_many[2] = {1, 2, 3};      // error: excess elements in array initializer
char small[2] = "abc";            // error: initializer-string for char array is too long
int from_string[4] = "abc";       // error: must be initialized with a brace-enclosed list
void holes[3];                    // error: has incomplete element type 'void'

int main() {
    int a[3], b[3], x = 0;
    int grid[2][2];
    double d = 1.0;
    x[0] = 1;                     // error: subscripted value is not an array or pointer
    a[d] = 1;                     // error: array subscript is not an integer
    grid[0][1][2] = 3;            // error: subscripted value is not an array or pointer
    a = b;                        // error: array type 'int[3]' is not assignable
    grid[0] = a;                  // error: array type 'int[2]' is not assignable
    int c[2] = 5;                 // error: must be initialized with a brace-enclosed list
    int s = {1, 2};               // error: excess elements in scalar initializer
    return a[1];
}
