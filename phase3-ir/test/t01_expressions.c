/* t01 -- operators: arithmetic, the slides' b * -c + b * -c, int/float/double
   conversions, unsigned, bitwise tricks, compound assignment, ++/--, comma,
   ?:, casts (C-style and functional), sizeof, scalar brace and paren
   initialization, wrap-around of every width. Expected: g++. */
int main() {
    int a = 7, b = 2, c = 3, x;
    x = b * -c + b * -c;
    printf("%d %d %d %d %d\n", x, a + b * c, (a + b) * c, a / b, a % b);
    double d = a;
    float f = a / 2;
    int back = (int)(d / 2 + 0.75);
    printf("%.2f %.1f %d %.3f\n", d / b, f, back, (float)a / 3);
    unsigned u = 10;
    printf("%u %u %d\n", u - 11, u * 3 / 4, (int)(u >> 1));
    int v = 0xB6;
    int bits = 0, t = v;
    while (t) { bits += t & 1; t >>= 1; }
    printf("%d %d %d %x %x\n", bits, (v & (v - 1)) == 0, (64 & 63) == 0, v ^ 0xFF, ~v & 0xFF);
    x = 5;
    x += 3; x -= 1; x *= 4; x /= 3; x %= 5; x <<= 3; x >>= 1; x |= 1; x &= 13; x ^= 6;
    printf("%d\n", x);
    int i = 5, j = i++ + 1, k = --i * 2;
    printf("%d %d %d\n", i, j, k);
    int m = (i = 3, i * 4);
    printf("%d %d %d\n", m, i > 2 ? 10 : 20, a < b ? a : b < c ? b : c);
    printf("%d %d %d\n", (int)sizeof(int), (int)sizeof(double), (int)sizeof(char));
    char ch = (char)130;
    unsigned char uch = (unsigned char)300;
    short sh = (short)65537;
    printf("%d %d %d %d\n", ch, uch, sh, (char)(ch + 200));
    printf("%d %d\n", -7 >> 1, (unsigned)-8 >> 29);
    int z = {}, w(5), q = {6};
    double dd = double(a) / 2 - 0.25;
    printf("%d %d %d %d %.2f %d\n", z, w, q, int(2.7), dd - 1.25, int());
    return 0;
}
