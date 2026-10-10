/* Unnamed class objects: each is destroyed at the end of the full
   expression that made it, unless it became a variable or the result of
   the function. Also `obj.Base::member` and `long long` arithmetic that
   stays in registers. Expected output: g++. */
#include <stdio.h>

class Tag {
  public:
    int id;
    Tag(int n) { id = n; printf("+%d ", id); }
    ~Tag() { printf("-%d ", id); }
    int value() { return id * 10; }
    Tag operator+(const Tag &o) { return Tag(id + o.id); }
};

class Copy {
  public:
    int id;
    Copy(int n) { id = n; printf("+c%d ", id); }
    Copy(const Copy &o) { id = o.id + 100; printf("copy%d ", id); }
    ~Copy() { printf("-c%d ", id); }
};

Tag make(int n) { return Tag(n); }
Tag named(int n) {
    Tag t(n);
    t.id = t.id + 1;
    return t; /* the result itself: not destroyed here */
}
Tag pick(int which) { /* two different locals: each is copied out, then destroyed */
    Tag a(40);
    Tag b(41);
    if (which) return a;
    return b;
}
int byValue(Tag t) { return t.id; }
int byRef(const Tag &t) { return t.id; }
int copied(Copy c) { return c.id; }
Copy makeCopy(int n) { return Copy(n); }
Copy sameCopy(Copy c) { return c; } /* a parameter is copied out */

class Shape {
  public:
    int sides() { return 0; }
    int kind() { return 1; }
};
class Square : public Shape {
  public:
    int sides() { return 4; }
    int kind() { return 2; }
};

long long mix(long long a, long long b, int n) {
    long long sum = 0;
    for (int i = 0; i < n; i++) {
        sum = sum + a * i - (b ^ sum);
        a = a + 0x100000000LL;
        b = -b + (sum & 0xFFFF);
    }
    return sum + a - b;
}

int main() {
    Tag(1);
    printf("| ");
    make(2);
    printf("| ");
    int v = Tag(3).value() + make(4).value();
    printf("%d | ", v);
    Tag kept = make(5); /* becomes `kept`: lives to the end of main */
    printf("| ");
    Tag sum = kept + Tag(6);
    printf("%d | ", sum.id);
    v = (kept + sum + kept).id; /* two temporaries, destroyed last-made first */
    printf("%d | ", v);
    v = byValue(Tag(10));
    printf("%d | ", v);
    v = byValue(kept); /* the parameter is a copy: destroyed after the call */
    printf("%d | ", v);
    v = byRef(Tag(11));
    printf("%d | ", v);
    if (byRef(Tag(12)) > 5) printf("if ");
    printf("| ");
    for (int i = 0; i < 2 && make(13 + i).id > 0; i = i + byRef(Tag(20))) printf("body ");
    printf("| ");
    v = v > 0 ? Tag(21).id : Tag(22).id;
    printf("%d | ", v);
    Tag n = named(30);
    printf("%d | ", n.id);
    v = pick(1).id;
    v = v + pick(0).id;
    printf("%d | ", v);
    const Tag &r = Tag(50); /* bound to a reference: lives as long as r */
    printf("%d | ", r.id);
    kept = Tag(60); /* assigned from: the temporary still dies here */
    printf("%d\n", kept.id);

    Copy c(1);
    printf("| ");
    v = copied(c);
    printf("%d | ", v);
    v = copied(Copy(2));
    printf("%d | ", v);
    Copy d = makeCopy(3);
    printf("%d | ", d.id);
    Copy e = sameCopy(c);
    printf("%d\n", e.id);

    Square q;
    Shape *p = &q;
    printf("%d %d %d %d %d %d\n", q.sides(), q.Shape::sides(), p->sides(), p->Shape::sides(), q.kind(), q.Shape::kind());

    long long m = mix(3, 5, 20);
    printf("%lld %lld\n", m, mix(-7, 1LL << 40, 9));
    {
        Tag inner(70);
        printf("%d ", byRef(inner) + byRef(Tag(71)));
    }
    printf("end\n");
    return 0;
}
