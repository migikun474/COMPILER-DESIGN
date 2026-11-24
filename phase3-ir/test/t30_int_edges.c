/* t30 -- integer edge cases: division and remainder with negative
   operands (truncation toward zero), shifts of signed and unsigned values,
   unsigned wrap-around, char/short sign and zero extension, signed vs
   unsigned comparison, the largest and smallest int. Expected: g++. */
int main() {
    int a = -7, b = 2, big = 2147483647, small = -2147483647 - 1;
    printf("%d %d %d %d\n", a / b, a % b, 7 / -2, 7 % -2);
    printf("%d %d %d\n", -a / -b, -8 / 3, -8 % 3);
    printf("%d %d %u %u\n", a >> 1, a << 2, (unsigned)a >> 28, 1u << 31);
    unsigned u = 0;
    u = u - 1;
    printf("%u %u %d\n", u, u + 2, (int)(u / 2));
    char c = (char)200;
    unsigned char uc = (unsigned char)200;
    short s = (short)40000;
    unsigned short us = (unsigned short)70000;
    printf("%d %d %d %d\n", c, uc, s, us);
    printf("%d %d\n", -1 < 0u, (unsigned)-1 > 5);
    printf("%d %d %u\n", big, small, (unsigned)big + 1u);
    int x = 1000;
    x = x * x * 3;
    printf("%d %d %d\n", x, x / 7 % 13, (x & 255) ^ 85);
    return 0;
}
