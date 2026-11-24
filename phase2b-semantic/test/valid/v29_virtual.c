/* valid: virtual functions (D44). A function that matches a virtual one of
   the base overrides it, with or without `virtual`; a class with a pure
   virtual function left without an overrider is abstract and is used only
   through pointers and references. */
class Shape {
public:
    virtual int area() = 0;
    virtual int sides() { return 0; }
    int twice() { return 2 * area(); }          /* a virtual call through this */
};
class Rect : public Shape {
public:
    int w, h;
    Rect() { w = 2; h = 3; }
    int area() { return w * h; }                /* overrides without the keyword */
    virtual int sides() { return 4; }
};
class Square : public Rect {
public:
    int area() { return w * w; }
};
int total(Shape &s, Shape *p) { return s.area() + p->sides() + p->Shape::sides(); }
Shape *pick(Rect *r) { return r; }
int main() {
    Square q;
    Rect r;
    Shape *all[2];
    all[0] = &q;
    all[1] = &r;
    Rect copy = r;                              /* same class: a plain copy */
    r = copy;
    return total(q, all[1]) + pick(&q)->twice() + copy.area();
}
