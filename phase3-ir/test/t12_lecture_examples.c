/* t12 -- the examples of Lectures 25-27, kept small so the listing in
   test/expected/t12_lecture_examples.tac can be read against the slides */
int main() {
    int a, b = 2, c = 3, d = 4, e = 5, f = 6, i = 1, x, y;
    int arr[10];
    int m[3][4];
    double r = 1.5;
    a = b * -c + b * -c;                 /* Lecture 25: a = b * -c + b * -c */
    while (a < b) a = a + 1;             /* Lecture 26/27: while E do S */
    if (a < b) x = 1; else x = 2;        /* if E then S1 else S2 */
    y = a < b;                           /* Lecture 27: id1 relop id2 as a value */
    y = a < b || c < d && e < f;         /* a < b or c < d and e < f */
    r = r + i;                           /* Lecture 26: inttoreal */
    x = arr[i];                          /* Lecture 26: base + i * w */
    m[i][2] = x;                         /* ((i1 * n2) + i2) * w */
    return y;
}
