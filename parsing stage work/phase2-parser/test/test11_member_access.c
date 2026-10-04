

struct Point {
    int x;
    int y;
};

class Dog {
public:
    int legs;
};

int main() {
    struct Point p;
    p.x = 1;
    p.y = 2;

    struct Point *pp;
    pp = &p;
    pp->x = 5;

    Dog d;
    d.legs = 4;

    return 0;
}
