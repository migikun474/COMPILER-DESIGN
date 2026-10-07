/* t05 -- pointers: levels, arithmetic, swap, void *, pointer to array */
#include <stdio.h>

void swap(int *a, int *b) {
    int t = *a;
    *a = *b;
    *b = t;
}

int sum(int *first, int *last) {
    int s = 0;
    while (first < last) s += *first++;
    return s;
}

int main() {
    int x = 5, y = 6;
    int *p = &x;
    int **pp = &p;
    int ***ppp = &pp;
    printf("%d %d %d\n", *p, **pp, ***ppp);
    **pp = 9;
    ***ppp += 1;
    swap(&x, &y);
    printf("%d %d\n", x, y);

    int arr[5] = {10, 20, 30, 40, 50};
    int *q = arr + 2;
    q = q - 1;
    int gap = (arr + 4) - q;
    printf("%d %d %d\n", *q, gap, sum(arr, arr + 5));
    q++;
    --q;
    q += 2;
    printf("%d %d %d\n", *q, q[-1], *(arr + 4));
    printf("%d %d %d\n", q == arr + 3, q != arr, q < arr + 4);

    void *raw = &x;
    int *back = (int *) raw;
    char *bytes = (char *) &y;
    *back = 258;
    printf("%d %d\n", x, *bytes);

    int grid[2][3] = {{1, 2, 3}, {4, 5, 6}};
    int (*row)[3] = grid;
    row = row + 1;
    printf("%d %d\n", (*row)[2], row[0][0]);

    p = 0;
    if (!p) p = &y;
    double d = 2.5, *dp = &d;
    *dp = *dp * 2;
    char text[] = "pointer";
    char *t = text;
    while (*t) t++;
    printf("%.1f %d %c\n", d, (int) (t - text), *(t - 1));
    return *p;
}
