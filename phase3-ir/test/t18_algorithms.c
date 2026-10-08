/* t18 -- classic algorithms: sorting, searching, recursion, matrices, primes */
#include <stdio.h>

void bubble(int a[], int n) {
    for (int i = 0; i < n - 1; i++)
        for (int j = 0; j < n - 1 - i; j++)
            if (a[j] > a[j + 1]) { int t = a[j]; a[j] = a[j + 1]; a[j + 1] = t; }
}

void quick(int a[], int lo, int hi) {
    if (lo >= hi) return;
    int pivot = a[(lo + hi) / 2], i = lo, j = hi;
    while (i <= j) {
        while (a[i] < pivot) i++;
        while (a[j] > pivot) j--;
        if (i <= j) { int t = a[i]; a[i] = a[j]; a[j] = t; i++; j--; }
    }
    quick(a, lo, j);
    quick(a, i, hi);
}

int search(int a[], int n, int key) {
    int lo = 0, hi = n - 1;
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;
        if (a[mid] == key) return mid;
        if (a[mid] < key) lo = mid + 1; else hi = mid - 1;
    }
    return -1;
}

int moves = 0;
void hanoi(int n, int from, int to, int via) {
    if (n == 0) return;
    hanoi(n - 1, from, via, to);
    moves++;
    hanoi(n - 1, via, to, from);
}

int ackermann(int m, int n) {
    if (m == 0) return n + 1;
    if (n == 0) return ackermann(m - 1, 1);
    return ackermann(m - 1, ackermann(m, n - 1));
}

void multiply(int a[2][3], int b[3][2], int c[2][2]) {
    for (int i = 0; i < 2; i++)
        for (int j = 0; j < 2; j++) {
            c[i][j] = 0;
            for (int k = 0; k < 3; k++) c[i][j] += a[i][k] * b[k][j];
        }
}

int primes(int limit) {
    char composite[101];
    int count = 0;
    for (int i = 0; i <= limit; i++) composite[i] = 0;
    for (int i = 2; i <= limit; i++) {
        if (composite[i]) continue;
        count++;
        for (int j = i * i; j <= limit; j += i) composite[j] = 1;
    }
    return count;
}

int power(int base, int exp) {
    int result = 1;
    while (exp > 0) {
        if (exp & 1) result *= base;
        base *= base;
        exp >>= 1;
    }
    return result;
}

int collatz(int n) { int steps = 0; while (n != 1) { n = n % 2 ? 3 * n + 1 : n / 2; steps++; } return steps; }

int main() {
    int a[8] = {42, 7, 19, 3, 25, 7, 88, 1}, b[8] = {5, -2, 9, 0, 9, 14, -7, 3};
    bubble(a, 8);
    quick(b, 0, 7);
    for (int i = 0; i < 8; i++) printf("%d ", a[i]);
    printf("\n");
    for (int i = 0; i < 8; i++) printf("%d ", b[i]);
    printf("\n%d %d %d\n", search(a, 8, 25), search(a, 8, 26), search(b, 8, -7));
    hanoi(6, 1, 3, 2);
    printf("%d %d %d\n", moves, ackermann(2, 3), collatz(27));
    int x[2][3] = {{1, 2, 3}, {4, 5, 6}}, y[3][2] = {{7, 8}, {9, 10}, {11, 12}}, z[2][2];
    multiply(x, y, z);
    printf("%d %d %d %d\n", z[0][0], z[0][1], z[1][0], z[1][1]);
    printf("%d %d %d\n", primes(100), power(3, 13), power(2, 10));
    return search(a, 8, 88);
}
