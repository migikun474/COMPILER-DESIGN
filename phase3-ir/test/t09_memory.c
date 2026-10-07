/* t09 -- dynamic memory: malloc / calloc / realloc / free, new[] / delete[],
   a linked list and a growing array */
#include <stdio.h>
#include <stdlib.h>

struct Node { int value; struct Node *next; };

struct Node *push(struct Node *head, int v) {
    struct Node *n = (struct Node *) malloc(sizeof(struct Node));
    n->value = v;
    n->next = head;
    return n;
}

int main() {
    int n = 5;
    int *a = (int *) malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) a[i] = i * i;
    int *z = (int *) calloc(n, sizeof(int));
    z[2] = a[4] + z[1];
    a = (int *) realloc(a, 2 * n * sizeof(int));
    for (int i = n; i < 2 * n; i++) a[i] = a[i - n] + 100;
    printf("%d %d %d %d\n", a[4], a[9], z[2], z[0]);

    struct Node *list = 0;
    for (int i = 1; i <= 4; i++) list = push(list, i * 10);
    int sum = 0;
    for (struct Node *p = list; p; p = p->next) sum += p->value;
    printf("%d %d\n", sum, list->next->value);
    while (list) {
        struct Node *dead = list;
        list = list->next;
        free(dead);
    }

    double *d = new double[3];
    d[0] = 1.5; d[1] = 2.5; d[2] = d[0] + d[1];
    int *one = new int;
    *one = 42;
    char *text = (char *) malloc(8);
    text[0] = 'o'; text[1] = 'k'; text[2] = 0;
    printf("%.1f %d %s\n", d[2], *one, text);
    delete[] d;
    delete one;
    free(text);
    free(a);
    free(z);
    return sum / 10;
}
