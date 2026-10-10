/* Storage classes: extern (declares an object defined elsewhere, or later)
   alongside static and typedef. */
extern int limit;
extern int lookup[];
extern int scale(int factor);
int lookup[3] = { 1, 2, 4 };
int limit = 3;

int scale(int factor) {
    extern int limit;              /* the file-scope limit */
    int k;
    int sum = 0;
    for (k = 0; k < limit; k++) sum += lookup[k] * factor;
    return sum;
}

static int calls;
typedef unsigned long counter_t;

int main() {
    counter_t n = 0;
    int r = scale(2);
    calls++;
    n = n + r + calls;
    return (int)n;
}
