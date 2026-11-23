/* The rules of Papaspyrou's formal semantics of C that were missing,
   with gcc's diagnostics at gcc's lines. */

struct Key { const int id; int v; };
struct Wrap { struct Key k; int n; };

int over1[2147483647 + 1];             // warning: integer overflow in expression of type 'int' results in '-2147483648'  // error: array size must be greater than zero
int shift1 = 1 << 32;                  // warning: left shift count >= width of type 'int'
int shift2 = 1 >> -1;                  // warning: right shift count is negative
char narrow = 300;                     // warning: overflow in conversion from 'int' to 'char' changes value from '300' to '44'
unsigned char unarrow = 256;           // warning: unsigned conversion from 'int' to 'unsigned char' changes value from '256' to '0'

struct Fwd;
int bad = sizeof(struct Fwd);          // error: invalid application of 'sizeof' to an incomplete type
int x = 1;
double x;                              // error: duplicate declaration of 'x'
static static int z;                   // error: multiple storage classes in the declaration of 'z'

int main() {
    struct Key k1 = { 1, 2 }, k2 = { 3, 4 };
    struct Wrap w1, w2;
    k1 = k2;                           // error: cannot assign to variable 'k1' of type 'struct Key': its member 'id' is const-qualified
    w1 = w2;                           // error: its member 'k.id' is const-qualified
    int i = 0, j, a[4];
    i = i++;                           // warning: operation on 'i' may be undefined
    a[i] = i++;                        // warning: operation on 'i' may be undefined
    j = i++ + i++;                     // warning: operation on 'i' may be undefined
    j = (i = 1) + i;                   // warning: operation on 'i' may be undefined
    printf("%d %d\n", i++, i++);       // warning: operation on 'i' may be undefined
    long l = 1; double d = 2; char c;
    printf("%d\n", l);                 // warning: format '%d' expects 'int', but argument 2 has type 'long'
    printf("%f\n", i);                 // warning: format '%f' expects a floating-point value
    scanf("%f", &d);                   // warning: format '%f' expects 'float *' (use '%lf' for a double)
    scanf("%d", &c);                   // warning: format '%d' expects 'int *', but argument 2 has type 'char *'
    return j + bad + narrow + unarrow + shift1 + shift2;
}
