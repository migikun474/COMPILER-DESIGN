/* t25 -- control flow in combination: a state machine in a switch,
   nested loops with break and continue, do-while, until, ?: chains,
   the comma operator, goto out of nested loops */
#include <stdio.h>
#ifdef __cplusplus
#define until(c) while (!(c))
#endif

int classify(const char *s) {                 /* 0 other, 1 integer, 2 decimal, 3 identifier */
    int state = 0;
    for (; *s; s++) {
        char c = *s;
        int digit = c >= '0' && c <= '9', letter = (c >= 'a' && c <= 'z') || c == '_';
        switch (state) {
            case 0:
                if (digit) state = 1;
                else if (letter) state = 3;
                else return 0;
                break;
            case 1:
                if (c == '.') state = 2;
                else if (!digit) return 0;
                break;
            case 2:
                if (!digit) return 0;
                break;
            case 3:
                if (!digit && !letter) return 0;
                break;
        }
    }
    return state;
}

int daysIn(int month, int year) {
    switch (month) {
        case 4: case 6: case 9: case 11: return 30;
        case 2: return (year % 4 == 0 && year % 100 != 0) || year % 400 == 0 ? 29 : 28;
        default: return 31;
    }
}

const char *grade(int score) {
    return score >= 90 ? "A" : score >= 75 ? "B" : score >= 60 ? "C" : "F";
}

int firstPair(int target) {                   /* goto out of two loops */
    int i, j;
    for (i = 1; i < 10; i++)
        for (j = i; j < 10; j++)
            if (i * j == target) goto found;
    return -1;
found:
    return i * 10 + j;
}

int main() {
    printf("%d %d %d %d %d\n", classify("1234"), classify("12.5"), classify("x_9"), classify("9x"), classify(""));
    printf("%d %d %d %d\n", daysIn(2, 2024), daysIn(2, 1900), daysIn(2, 2000), daysIn(11, 2023));
    printf("%s %s %s %s\n", grade(95), grade(80), grade(60), grade(10));
    printf("%d %d %d\n", firstPair(24), firstPair(49), firstPair(97));

    int triangle = 0, skipped = 0;
    for (int i = 1; i <= 6; i++) {
        if (i == 4) { skipped++; continue; }
        for (int j = 1; j <= 6; j++) {
            if (j > i) break;
            if ((i + j) % 2) continue;
            triangle += i * j;
        }
    }
    printf("%d %d\n", triangle, skipped);

    int n = 0, digits = 0, value = 90210;
    do { digits++; value /= 10; } while (value);
    until (n * n > 200) n++;
    int a, b, c;
    for (a = 0, b = 10; a < b; a++, b--) ;
    c = (a++, b += 2, a + b);
    printf("%d %d %d %d %d\n", digits, n, a, b, c);

    int steps = 0, k = 27;
    while (1) {
        if (k == 1) break;
        k = k % 2 ? 3 * k + 1 : k / 2;
        if (++steps > 200) break;
    }
    int countdown = 3;
    while (countdown --> 0) printf("%d ", countdown);
    printf("\n%d\n", steps);
    return digits;
}
