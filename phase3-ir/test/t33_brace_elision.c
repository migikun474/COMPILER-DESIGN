#include <stdio.h>
struct In { int x, y; };
struct S { int a[2]; int b; struct In in; char name[4]; };
struct S g = {1, 2, 3, 4, 5, "ab"};
struct In pts[] = {1, 2, 3, 4, 5};
int m[][3] = {1, 2, 3, 4};
int main() {
    struct S s = {1, 2, 3, 4, 5, "xy"};
    struct S t = {{7}, 8, {9}, "z"};
    struct In first = {6, 7};
    struct { struct In p; int z; } u = {first, 9};
    struct S d = {1, 2, .in = {3, 4}, "w"};
    printf("%d %d %d %d %d %s\n", g.a[0], g.a[1], g.b, g.in.x, g.in.y, g.name);
    printf("%d %d %d %d %d %s\n", s.a[0], s.a[1], s.b, s.in.x, s.in.y, s.name);
    printf("%d %d %d %d %d %s\n", t.a[0], t.a[1], t.b, t.in.x, t.in.y, t.name);
    printf("%d %d %d %d %d\n", (int) (sizeof(pts) / sizeof(pts[0])), pts[1].y, pts[2].x, pts[2].y, (int) (sizeof(m) / sizeof(m[0])));
    printf("%d %d %d %d %d %d %d\n", u.p.x, u.p.y, u.z, m[1][0], m[1][2], d.in.y, d.name[0]);
    return 0;
}
