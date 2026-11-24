/* t45 -- characters and strings by hand: walking a string with a
   pointer, copying and comparing, escapes, character arithmetic, case
   conversion, digits to a number and back, %c %s %5s %-5s %.2s.
   Expected: g++. */
int len(const char *s) { int n = 0; while (*s++) n++; return n; }
void copy(char *d, const char *s) { while ((*d++ = *s++)) { } }
int cmp(const char *a, const char *b) { while (*a && *a == *b) { a++; b++; } return *a - *b; }
int main() {
    char buf[32];
    copy(buf, "Hello\tWorld\n");
    printf("%d %d %d\n", len(buf), buf[5] == '\t', buf[len(buf) - 1] == '\n');
    printf("%d %d %d\n", cmp("abc", "abd") < 0, cmp("abc", "abc"), cmp("b", "a") > 0);
    char up[8] = "mips";
    int i;
    for (i = 0; up[i]; i++) up[i] = up[i] - 'a' + 'A';
    printf("%s %c %c\n", up, 'a' + 1, 'z' - 25);
    const char *digits = "40213";
    int value = 0;
    for (i = 0; digits[i]; i++) value = value * 10 + (digits[i] - '0');
    char out[8];
    int n = 0, v = value;
    while (v > 0) { out[n++] = (char)('0' + v % 10); v /= 10; }
    out[n] = 0;
    printf("%d %s\n", value, out);
    printf("[%5s] [%-5s] [%.2s] [%c]\n", "ab", "ab", "abcdef", 'Q');
    printf("%d %d\n", '\\', "quote\"d"[5]);
    return 0;
}
