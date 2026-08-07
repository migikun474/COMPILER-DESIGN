int main() {
    int a = 10, b = 3, c;
    c = a + b - (a * b) / b % a;
    if (a > b && b <= a || !(a == b) && a != b) {
        c = c & b | a ^ b;
        c = ~c;
        c <<= 2;
        c >>= 1;
    }
    c += 1;
    c -= 1;
    c *= 2;
    c /= 2;
    c %= 3;
    return 0;
}
