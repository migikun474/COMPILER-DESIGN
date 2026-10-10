/* t17 -- character arrays and strings handled by hand: length, copy,
   compare, reverse, search, number <-> text */
#include <stdio.h>

int length(const char *s) { int n = 0; while (s[n] != '\0') n++; return n; }

void copy(char *to, const char *from) { while ((*to++ = *from++) != '\0') ; }

int compare(const char *a, const char *b) {
    while (*a && *a == *b) { a++; b++; }
    return *a - *b;
}

void reverse(char *s) {
    int i = 0, j = length(s) - 1;
    while (i < j) { char t = s[i]; s[i] = s[j]; s[j] = t; i++; j--; }
}

int find(const char *text, char c) {
    for (int i = 0; text[i]; i++) if (text[i] == c) return i;
    return -1;
}

int toNumber(const char *s) {
    int sign = 1, v = 0;
    if (*s == '-') { sign = -1; s++; }
    while (*s >= '0' && *s <= '9') { v = v * 10 + (*s - '0'); s++; }
    return sign * v;
}

void toText(int v, char *out) {
    char tmp[12];
    int n = 0, neg = v < 0;
    if (neg) v = -v;
    do { tmp[n++] = '0' + v % 10; v /= 10; } while (v > 0);
    if (neg) tmp[n++] = '-';
    while (n > 0) *out++ = tmp[--n];
    *out = '\0';
}

int isPalindrome(const char *s) {
    int i = 0, j = length(s) - 1;
    while (i < j) if (s[i++] != s[j--]) return 0;
    return 1;
}

int countWords(const char *s) {
    int words = 0, inside = 0;
    for (; *s; s++) {
        if (*s == ' ' || *s == '\t') inside = 0;
        else if (!inside) { inside = 1; words++; }
    }
    return words;
}

int main() {
    char buf[32], num[16];
    const char *names[3] = {"delta", "alpha", "charlie"};
    copy(buf, "compiler");
    printf("%s %d\n", buf, length(buf));
    reverse(buf);
    printf("%s %d %d\n", buf, find(buf, 'p'), find(buf, 'z'));
    printf("%d %d %d\n", compare("abc", "abd") < 0, compare("abc", "abc"), compare("b", "abc") > 0);
    int smallest = 0;
    for (int i = 1; i < 3; i++) if (compare(names[i], names[smallest]) < 0) smallest = i;
    printf("%s %c\n", names[smallest], names[2][3]);
    toText(-40213, num);
    printf("%s %d %d\n", num, toNumber(num) + 1, toNumber("77x"));
    printf("%d %d %d\n", isPalindrome("level"), isPalindrome("lever"), countWords("  the quick  brown fox "));
    char upper[8] = "mixed";
    for (int i = 0; upper[i]; i++) if (upper[i] >= 'a' && upper[i] <= 'z') upper[i] = upper[i] - 'a' + 'A';
    printf("%s %d\n", upper, (int) sizeof(upper));
    return length(names[1]) + buf[0];
}
