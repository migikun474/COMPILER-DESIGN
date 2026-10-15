/* virtual functions: tables, overriding at several levels, multiple
   inheritance (this-adjustment), calls from constructors and
   destructors, references, slicing, abstract classes. Expected: g++. */
#include <stdio.h>

class Animal {
  public:
    int legs;
    Animal(int n) : legs(n) { printf("[A %s] ", name()); }
    virtual ~Animal() { printf("[~A %s] ", name()); }
    virtual const char *name() const { return "animal"; }
    virtual int speed() { return legs; }
    int describe() { return speed() * 10 + legs; }  /* a virtual call through this */
};

class Dog : public Animal {
  public:
    int bark;
    Dog(int b) : Animal(4), bark(b) { printf("[D %s] ", name()); }
    ~Dog() { printf("[~D %s] ", name()); }
    const char *name() const { return "dog"; }
    int speed() { return 12 + bark; }
};

class Puppy : public Dog {
  public:
    Puppy() : Dog(1) { }
    const char *name() const { return "puppy"; }  /* speed() is still Dog's */
};

class Swimmer {
  public:
    int depth;
    Swimmer() : depth(3) { }
    virtual int swim() { return depth; }
    virtual int dive(int m) { return depth + m; }
};

class Seal : public Animal, public Swimmer {  /* Swimmer is a second base: its own table */
  public:
    int fat;
    Seal() : Animal(0), fat(7) { }
    const char *name() const { return "seal"; }
    int swim() { return fat * 2 + depth; }      /* reached through a Swimmer *: `this` moves back */
};

class Shape {
  public:
    virtual int area() = 0;
    virtual int sides() { return 0; }
    int twice() { return area() * 2; }
};
class Rect : public Shape {
  public:
    int w, h;
    Rect(int a, int b) : w(a), h(b) { }
    int area() { return w * h; }
    int sides() { return 4; }
};
class Square : public Rect {
  public:
    Square(int s) : Rect(s, s) { }
    int area() { return Rect::area() + 1; }   /* a qualified call is not virtual */
};

int total(Shape &s) { return s.area() + s.sides(); }
int race(Animal *a) { return a->speed(); }

int main() {
    Dog d(5);
    printf("\n");
    Puppy p;
    printf("\n");
    Animal *zoo[3] = {&d, &p, 0};
    Seal s;
    zoo[2] = &s;
    printf("\n");
    for (int i = 0; i < 3; i++) printf("%s %d %d | ", zoo[i]->name(), zoo[i]->speed(), zoo[i]->describe());
    printf("\n");
    Swimmer *w = &s;
    printf("%d %d %d\n", w->swim(), w->dive(2), race(&s));
    Animal &ref = p;
    printf("%s %d %d\n", ref.name(), ref.Animal::speed(), d.Animal::speed());
    Animal copy = d;               /* slicing: a plain Animal */
    printf("%s %d\n", copy.name(), copy.speed());
    copy = p;                      /* assignment keeps it an Animal */
    printf("%s %d\n", copy.name(), copy.speed());
    Rect r(2, 3);
    Square sq(4);
    Shape *shapes[2] = {&r, &sq};
    for (int i = 0; i < 2; i++) printf("%d %d %d | ", shapes[i]->area(), shapes[i]->twice(), total(*shapes[i]));
    printf("\n");
    return 0;
}
