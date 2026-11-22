/* t08 -- classes: methods, default constructors in order (base, members,
   own body), single inheritance, static members, operator overloading,
   arrays of objects */

class Animal {
public:
    int legs;
    Animal() { legs = 4; printf("Animal()\n"); }
    int count() { return legs; }
};

class Tag {
public:
    int id;
    Tag() { id = 7; printf("Tag()\n"); }
};

class Dog : public Animal {
public:
    int age;
    Tag tag;
    static int made;
    Dog() { age = 0; made++; printf("Dog()\n"); }
    int human() { return age * 7 + legs + this->tag.id; }
    void birthday();
    static int total() { return made; }
};
int Dog::made = 0;
void Dog::birthday() { age = age + 1; }

class Vec {
public:
    int x;
    int y;
    Vec() { x = 0; y = 0; }
    Vec operator+(Vec o) { Vec r; r.x = x + o.x; r.y = y + o.y; return r; }
    Vec operator-() { Vec r; r.x = -x; r.y = -y; return r; }
    int operator==(Vec o) { return x == o.x && y == o.y; }
    int operator[](int i) { return i == 0 ? x : y; }
    Vec &operator+=(Vec o) { x += o.x; y += o.y; return *this; }
    Vec &operator++() { x++; return *this; }
    int operator()(int k) { return x * k + y; }
    int dot(Vec o) { return x * o.x + y * o.y; }
};
Vec make(int a, int b) { Vec v; v.x = a; v.y = b; return v; }
Vec operator*(Vec v, int k) { return make(v.x * k, v.y * k); }

int main() {
    {
        Dog rex;
        rex.age = 3;
        rex.birthday();
        printf("%d %d %d\n", rex.human(), rex.count(), Dog::total());
        Animal *base = &rex;
        printf("%d\n", base->legs);
    }
    printf("--\n");
    {
        Dog other;
        other.age = 5;
        printf("%d %d\n", other.human(), Dog::made);
    }
    printf("--\n");

    Vec a = make(1, 2), b = make(3, 4), c;
    c = a + b;
    Vec d = -c;
    Vec e = a * 3;
    a += b;
    ++a;
    printf("%d %d %d %d %d %d\n", c.x, c.y, d.x, e.y, a.x, a.y);
    printf("%d %d %d %d %d\n", a == b, c == c, a[0], a(2), a.dot(b));
    Vec row[2];
    row[1].x = 9;
    printf("%d %d\n", row[0].x, row[1].x);
    int w(7);
    return w + c.x;
}
