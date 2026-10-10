/* t22 -- pointers and dynamic data: linked list, binary tree, stack,
   array of pointers, a table allocated row by row */
#include <stdio.h>
#include <stdlib.h>

struct Node { int value; struct Node *next; };
struct Tree { int key; struct Tree *left; struct Tree *right; };
typedef struct { int items[8]; int top; } Stack;

struct Node *prepend(struct Node *head, int v) {
    struct Node *n = (struct Node *) malloc(sizeof(struct Node));
    n->value = v;
    n->next = head;
    return n;
}

struct Node *reverse(struct Node *head) {
    struct Node *prev = 0;
    while (head) {
        struct Node *next = head->next;
        head->next = prev;
        prev = head;
        head = next;
    }
    return prev;
}

void removeValue(struct Node **link, int v) {
    while (*link) {
        if ((*link)->value == v) { struct Node *dead = *link; *link = dead->next; free(dead); }
        else link = &(*link)->next;
    }
}

struct Tree *insert(struct Tree *t, int key) {
    if (!t) {
        t = (struct Tree *) malloc(sizeof(struct Tree));
        t->key = key;
        t->left = t->right = 0;
    } else if (key < t->key) t->left = insert(t->left, key);
    else t->right = insert(t->right, key);
    return t;
}

void inorder(struct Tree *t) {
    if (!t) return;
    inorder(t->left);
    printf("%d ", t->key);
    inorder(t->right);
}

int height(struct Tree *t) {
    if (!t) return 0;
    int l = height(t->left), r = height(t->right);
    return 1 + (l > r ? l : r);
}

void push(Stack *s, int v) { s->items[s->top++] = v; }
int pop(Stack *s) { return s->items[--s->top]; }

int main() {
    struct Node *list = 0;
    for (int i = 1; i <= 6; i++) list = prepend(list, i * i % 7);
    list = reverse(list);
    removeValue(&list, 2);
    for (struct Node *p = list; p; p = p->next) printf("%d ", p->value);
    printf("\n");

    struct Tree *root = 0;
    int keys[7] = {50, 30, 70, 20, 40, 60, 80};
    for (int i = 0; i < 7; i++) root = insert(root, keys[i]);
    root = insert(root, 10);
    inorder(root);
    printf("\n%d %d %d\n", height(root), root->left->left->left->key, root->right->left->key);

    Stack s;
    s.top = 0;
    for (int i = 0; i < 5; i++) push(&s, i * 3);
    int a = pop(&s), b = pop(&s);
    printf("%d %d %d\n", a, b, s.top);

    int rows = 3, cols = 4;
    int **table = (int **) malloc(rows * sizeof(int *));
    for (int r = 0; r < rows; r++) {
        table[r] = (int *) malloc(cols * sizeof(int));
        for (int c = 0; c < cols; c++) table[r][c] = r * 10 + c;
    }
    int diagonal = 0;
    for (int r = 0; r < rows; r++) diagonal += table[r][r];
    int *last = table[rows - 1] + cols - 1;
    printf("%d %d %d\n", diagonal, *last, *(*(table + 1) + 2));

    int v1 = 1, v2 = 2, v3 = 3;
    int *ptrs[3] = {&v3, &v1, &v2};
    int **pp = ptrs;
    **pp = 30;
    *ptrs[2] += 5;
    printf("%d %d %d %d\n", v1, v2, v3, **(pp + 1));
    return height(root);
}
