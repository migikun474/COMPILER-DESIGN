/* t04 -- arrays: 1-D, 2-D and 3-D with initializers, partial and
   designated initializers, zeroed static data, i[a], an indexed literal,
   arrays passed to functions (1-D and 2-D), char arrays as strings,
   sizeof of an array. Plain C (g++ rejects the [4] designator): expected
   output from gcc. */
int zero[5];
int sum(int a[], int n) { int s = 0, i; for (i = 0; i < n; i++) s += a[i]; return s; }
int trace(int m[3][3]) { return m[0][0] + m[1][1] + m[2][2]; }
int main() {
    int a[6] = {4, 8, [4] = 1};
    int m[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int cube[2][2][2] = {{{1, 2}, {3, 4}}, {{5, 6}, {7, 8}}};
    printf("%d %d %d %d\n", sum(a, 6), a[3], a[4], 2[a]);
    printf("%d %d %d\n", trace(m), m[2][0] * m[0][2], cube[1][0][1]);
    int i, j, s = 0;
    for (i = 0; i < 3; i++) for (j = 0; j < 3; j++) m[i][j] = i * 3 + j;
    for (i = 0; i < 3; i++) s += m[i][2 - i];
    printf("%d %d %c\n", s, zero[3], "xyz"[1]);
    char word[8] = "hey";
    word[3] = '!';
    printf("%s %d %d\n", word, (int)sizeof(word), (int)sizeof(m) / (int)sizeof(m[0]));
    return 0;
}
