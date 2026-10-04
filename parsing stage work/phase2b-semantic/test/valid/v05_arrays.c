/* valid: int/char arrays, multidimensional arrays, initializer lists,
   arrays as parameters [test 17] */
int sum(int a[], int n) {         /* `int a[]` is `int *a` */
    int s = 0;
    for (int i = 0; i < n; i++) s += a[i];
    return s;
}

int trace(int m[3][3]) { return m[0][0] + m[1][1] + m[2][2]; }

int main() {
    int a[5] = {1, 2, 3, 4, 5};
    int z[5] = {1};               /* the rest are zero */
    char name[10] = "abc";
    char exact[3] = "abc";        /* fills the array exactly (no NUL), as C allows */
    char chars[4] = {'a', 'b', 'c', '\0'};
    int grid[3][3] = {{1, 0, 0}, {0, 1, 0}, {0, 0, 1}};
    int flat[2][2] = {1, 2, 3, 4};   /* braces may be elided */
    int cube[2][3][4];
    int i = 2;

    a[0] = 10;
    a[i] = a[i - 1] + a[i + 1];
    grid[1][2] = grid[2][1];
    cube[1][2][3] = 7;
    name[0] = 'A';
    i = 1[a];                     /* a[1] spelled the other way round */
    char c = "literal"[2];
    int *p = a;                   /* array decays to a pointer */
    p = grid[1];
    return sum(a, 5) + trace(grid) + z[1] + chars[0] + exact[2] + flat[1][1] + c + *p;
}
