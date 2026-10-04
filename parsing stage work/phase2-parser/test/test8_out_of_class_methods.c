

class Dog {
public:
    int legs;
    int bark();
};

int Dog::bark() {
    return legs;
}

int main() {
    Dog d;
    int b;
    b = d.bark();
    return 0;
}
