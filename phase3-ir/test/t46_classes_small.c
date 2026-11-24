/* t46 -- classes in a few lines: constructor order down a chain, a static
   member counting objects, a virtual and a non-virtual function with the
   same names, an operator returning a reference, an array of objects
   built by the default constructor. Expected: g++. */
class Base {
public:
    static int made;
    int v;
    Base() { v = 1; made++; printf("Base "); }
    virtual int who() { return 1; }
    int plain() { return 10; }
};
int Base::made = 0;
class Mid : public Base {
public:
    Mid() { v = v + 1; printf("Mid "); }
    int who() { return 2; }
    int plain() { return 20; }
};
class Leaf : public Mid {
public:
    Leaf() { v = v * 10; printf("Leaf\n"); }
    int who() { return 3; }
    Leaf &operator+=(int k) { v = v + k; return *this; }
};
int main() {
    Leaf l;
    Base *b = &l;
    Mid *m = &l;
    printf("%d %d %d %d %d\n", l.v, b->who(), m->who(), b->plain(), m->plain());
    (l += 5) += 2;
    printf("%d\n", l.v);
    Mid arr[2];
    printf("\n%d %d\n", Base::made, arr[1].who());
    return 0;
}
