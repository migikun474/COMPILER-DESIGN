/* t10 -- printf formats and scanf (input: test/t10_io.in) */
#include <stdio.h>

int main() {
    int n, total = 0;
    double scale;
    char name[16];
    char grade;
    scanf("%d %lf %15s %c", &n, &scale, name, &grade);
    for (int i = 0; i < n; i++) {
        int v;
        scanf("%d", &v);
        total += v;
    }
    printf("%s %c %d %.2f\n", name, grade, total, total * scale);
    printf("[%5d] [%-5d] [%05d] [%x] [%o] [%c] [%%]\n", 42, 42, 42, 255, 8, 'z');
    printf("[%8.3f] [%-8.1f] [%e] [%10s] [%-6s]\n", 3.14159, 2.5, 12345.678, "right", "left");
    printf("%u %lld %d\n", 3000000000u, 9000000000LL, -5);
    float f = 1.25f;
    char c = 'q';
    short s = -3;
    printf("%.2f %c %d\n", f, c, s);
    return total;
}
