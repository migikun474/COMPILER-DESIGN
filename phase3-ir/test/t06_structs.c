/* t06 -- structures: nesting, arrays of structs, pointers, copies,
   by-value parameters and results, initializers, anonymous members */
#include <stdio.h>

struct Point { int x; int y; };
struct Rect { struct Point low; struct Point high; char tag; };
struct Node { int value; struct Node *next; };
typedef struct { double re; double im; } Complex;
struct Packet {
    int kind;
    struct { int word; char bytes[4]; };
    short tail;
};

struct Point make(int x, int y) {
    struct Point p = {x, y};
    return p;
}

int area(struct Rect r) {
    r.high.x = r.high.x - r.low.x;       /* a copy: the caller's object is unchanged */
    return r.high.x * (r.high.y - r.low.y);
}

void move(struct Point *p, int dx) { p->x += dx; }

Complex add(Complex a, Complex b) {
    Complex c;
    c.re = a.re + b.re;
    c.im = a.im + b.im;
    return c;
}

int length(struct Node *head) {
    int n = 0;
    while (head) { n++; head = head->next; }
    return n;
}

struct Point origin = {3, 4};

int main() {
    struct Rect r = {{1, 2}, {5, 8}, 'r'};
    struct Rect copy;
    copy = r;
    copy.low.x = 100;
    printf("%d %d %d %c\n", r.low.x, copy.low.x, area(r), r.tag);
    printf("%d %d\n", r.high.x, origin.x * origin.y);

    struct Point pts[3];
    for (int i = 0; i < 3; i++) pts[i] = make(i, i * i);
    move(&pts[1], 10);
    (&pts[2])->y += 1;
    printf("%d %d %d %d\n", pts[1].x, pts[1].y, pts[2].y, make(3, 4).y);

    struct Point *pp = &r.high;
    pp->x = pp->y + 1;
    struct Rect *rp = &r;
    rp->low = make(7, 7);
    printf("%d %d %d\n", r.high.x, rp->low.x, rp->high.y);

    Complex a = {1.5, 2.0}, b = {.im = 0.5, .re = 1.0};
    Complex c = add(a, b);
    printf("%.1f %.1f\n", c.re, c.im);

    struct Node n1, n2, n3;
    n1.value = 1; n1.next = &n2;
    n2.value = 2; n2.next = &n3;
    n3.value = 3; n3.next = 0;
    printf("%d %d\n", length(&n1), n1.next->next->value);

    struct Packet k = {1, {0x01020304}, 9};
    k.bytes[1] = 'x';
    printf("%d %d %c %d %d\n", k.kind, k.word, k.bytes[1], k.tail, (int) sizeof(struct Packet));
    struct Point zero = {};
    return zero.x + pts[2].x;
}
