/* test30 -- class syntax: default constructors, single inheritance,
   friend declarations; and member names after any expression (arr[0].x,
   f().x, a.b.c, this->x), which the Token_Type table classifies. (The
   class syntax removed by D35 is in test31_dropped_class_features.c.) */
class Shape {
  public:
    int id;
    Shape() { id = 4; }
    int sides() { return 0; }
    friend int peek(const Shape &s);
    friend class Inspector;
};
class Square : public Shape {
    int side;
  public:
    Square() { side = 3; }
    int area() { return side * side; }
};
int peek(const Shape &s) { return s.id; }
int shapes() {
    Square q;
    Shape *p = &q;
    return q.area() + p->sides() + peek(q);
}
struct In { int v; };
struct P { int x; struct In in; struct In list[2]; };
struct P make() { struct P p; p.x = 1; return p; }
class Dog { public: int legs; Dog *next; int get() { return this->legs; } };
int use(struct P *q) { return q->x + q->in.v; }
int members() {
    struct P arr[3];
    struct P *p = arr;
    arr[0].x = 1;
    arr[1].in.v = 2;
    p->list[1].v = 3;
    (*p).x = 4;
    int a = make().x;
    Dog d;
    d.next = &d;
    d.next->legs = 4;
    return a + use(p) + d.next->next->legs;
}
int main() { return shapes() + members(); }
