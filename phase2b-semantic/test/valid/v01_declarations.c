/* valid: declarations, initialization, typedef, static, const, global
   constant initializers [test 1: valid variable declaration] */
typedef int Number;
typedef char *String;
typedef unsigned long Size;

int counter = 0;
int limit = 10 * 4 + 2;          /* constant expression */
static int hidden = -1;
const int MAX = 100;
char letter = 'z';
double ratio = 1.5 * 2;
int table[MAX];                  /* const int with a known value sizes an array */
int *where = &counter;           /* address of a global is a link-time constant */
char greeting[] = "hello";       /* size 6 deduced from the string */
int primes[] = {2, 3, 5, 7};     /* size 4 deduced from the list */
Size big = 4000000000u;

int next_id() {
    static int id = 0;           /* static local: constant initializer */
    id = id + 1;
    return id;
}

int main() {
    Number n = 5;
    String s = greeting;
    int a = 1, b = 2, c;
    unsigned int u = 3u;
    short sh = 2;
    long l = 7;
    signed char sc = -1;
    long long wide = 1;
    float f = 2.5f;
    bool done = false;
    c = a + b + n + u + sh + l + sc + wide + f + done;
    int local = sizeof(table) / sizeof(table[0]);
    char t = s[0];
    return c + local + t + next_id() + hidden + letter + primes[0];
}
