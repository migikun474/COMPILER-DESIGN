/* valid: obj.Base::member and ptr->Base::member name the member of that
   class, even when the object's own class hides it */
class Shape {
public:
    int corners;
    int sides() { return 0; }
    int kind() { return 1; }
};
class Square : public Shape {
public:
    int corners;
    int sides() { return 4; }
    int kind() { return 2; }
};

int main() {
    Square q;
    Square *p = &q;
    q.corners = 4;
    q.Shape::corners = 0;                 /* the hidden field of the base */
    p->Shape::corners = p->Shape::corners + 1;
    int a = q.sides() + q.Shape::sides(); /* 4 + 0 */
    int b = p->kind() + p->Shape::kind(); /* 2 + 1 */
    int c = q.Square::sides();            /* its own class may be named too */
    return a + b + c + q.corners + q.Shape::corners;
}
