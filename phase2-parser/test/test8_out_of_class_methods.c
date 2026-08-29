/* Out-of-class method definitions: `Dog::bark() {...}` should mangle
 * to the exact same name as the in-class prototype `int bark();`
 * declared inside `class Dog {...}` -- both are the same function. */

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
