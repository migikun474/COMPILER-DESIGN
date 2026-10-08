/* t20 -- bit manipulation and the edges of integer arithmetic */
#include <stdio.h>

int popcount(unsigned int v) { int n = 0; while (v) { n += v & 1; v >>= 1; } return n; }

unsigned int reverseBits(unsigned int v) {
    unsigned int r = 0;
    for (int i = 0; i < 32; i++) { r = (r << 1) | (v & 1); v >>= 1; }
    return r;
}

int isPowerOfTwo(unsigned int v) { return v != 0 && (v & (v - 1)) == 0; }
int highestBit(unsigned int v) { int n = -1; while (v) { v >>= 1; n++; } return n; }
unsigned int rotl(unsigned int v, int k) { return (v << k) | (v >> (32 - k)); }
int sign(int v) { return (v > 0) - (v < 0); }

int main() {
    unsigned int u = 0xF0F01234u;
    printf("%d %x %d %d %d\n", popcount(u), reverseBits(u), isPowerOfTwo(64), isPowerOfTwo(65), highestBit(1000));
    printf("%x %x %x %x\n", u & 0xFFFF, u | 0xF, u ^ 0xFFFFFFFFu, ~u);
    printf("%x %x %x\n", rotl(u, 8), u << 4, u >> 28);

    int big = 2147483647, small = -2147483647 - 1;
    unsigned int wrap = 4294967295u;
    wrap = wrap + 2;
    printf("%d %d %u %u\n", big, small, wrap, (unsigned int) small);
    printf("%d %d %d %d\n", small >> 31, -1 >> 1, (int) (0x80000000u >> 31), 1 << 30);

    unsigned char uc = 255;
    signed char sc = 127;
    short sh = -32768;
    unsigned short us = 65535;
    uc++; sc++; sh--; us++;
    printf("%d %d %d %d\n", uc, sc, sh, us);
    printf("%d %d %d\n", -7 / 2, -7 % 2, 7 / -2);
    printf("%d %d %d\n", -1 < 1u, -1 < 1, (unsigned int) -1 > 100u);
    printf("%d %d %d %d\n", sign(-9), sign(0), sign(4), !!12345);

    int flags = 0;
    flags |= 1 << 3;
    flags |= 1 << 0;
    flags &= ~(1 << 0);
    flags ^= 0x18;
    printf("%d %d\n", flags, (flags >> 4) & 1);
    char c = 'A';
    c |= 0x20;
    printf("%c %c %d\n", c, c ^ 0x20, 'z' - 'a');
    return popcount(255);
}
