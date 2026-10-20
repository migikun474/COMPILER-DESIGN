/* test30 -- class syntax added with the last batch: virtual and pure
   virtual functions, virtual destructors, explicit constructors, const
   member functions, friend declarations, member initializer lists; and
   member names after any expression (arr[0].x, f().x, a.b.c, this->x),
   which the Token_Type table now classifies. */
class Shape {
  public:
    int id;
    Shape(int n) : id(n) { }
    virtual int area() const { return 0; }
    virtual int sides() = 0;
    virtual ~Shape() { printf("~Shape%d ", id); }
    friend int peek(const Shape &s);
    friend class Inspector;
};
class Square : public Shape {
    int side;
  public:
    explicit Square(int s) : Shape(4), side(s) { }
    int area() const { return side * side; }
    int sides() { return 4; }
};
int peek(const Shape &s) { return s.id; }
int shapes() {
    Square q(3);
    Shape *p = &q;
    return p->area() + p->sides() + peek(q);
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
