/* t04 -- arrays: 1-D, 2-D, 3-D, initializers, strings, arrays as arguments */
#include <stdio.h>

int total(int a[], int n) {
    int s = 0;
    for (int i = 0; i < n; i++) s += a[i];
    return s;
}

int trace(int m[][3], int n) {
    int s = 0;
    for (int i = 0; i < n; i++) s += m[i][i];
    return s;
}

int length(char *s) {
    int n = 0;
    while (s[n]) n++;
    return n;
}

int squares[5];                          /* zero-initialized static data */
int table[2][3] = {{1, 2, 3}, {4, 5, 6}};

int main() {
    int a[5] = {1, 2, 3};
    int m[3][3];
    int cube[2][3][4];
    int i, j, k;
    for (i = 0; i < 5; i++) squares[i] = i * i;
    for (i = 0; i < 3; i++)
        for (j = 0; j < 3; j++) m[i][j] = i * 3 + j;
    for (i = 0; i < 2; i++)
        for (j = 0; j < 3; j++)
            for (k = 0; k < 4; k++) cube[i][j][k] = i * 100 + j * 10 + k;
    printf("%d %d %d %d %d\n", a[0], a[2], a[3], a[4], total(a, 5));
    printf("%d %d %d\n", squares[4], total(squares, 5), trace(m, 3));
    printf("%d %d %d\n", cube[1][2][3], cube[0][1][2], m[2][1]);
    printf("%d %d\n", table[1][2], table[0][1] + table[1][0]);

    int flat[2][2] = {1, 2, 3, 4};
    int sparse[6] = {[4] = 9, [1] = 7};
    int sized[] = {5, 6, 7, 8};
    printf("%d %d %d %d %d\n", flat[1][0], sparse[1], sparse[4], sparse[5], (int) (sizeof(sized) / sizeof(sized[0])));

    char word[] = "hello";
    char buf[8] = "ab";
    char *lit = "wide" " world";
    word[0] = 'j';
    buf[2] = 'c';
    printf("%s %s %s %d %d\n", word, buf, lit, length(word), length(lit));

    double avg[3] = {1.5, 2.5};
    avg[2] = (avg[0] + avg[1]) / 2;
    printf("%.2f\n", avg[2]);
    i = 2;
    a[i] = a[i - 1] + a[i + 1];
    a[a[0]] += 10;
    printf("%d %d\n", a[2], a[1]);
    return m[1][1];
}
