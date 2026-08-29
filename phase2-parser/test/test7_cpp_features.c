/* Newly added features: bool/const/volatile, sizeof/new/delete, class
 * inheritance, constructors/destructors, and class names usable
 * directly as types (the way real C++ works, unlike plain C where you
 * always need the `struct`/`class` keyword repeated). */

class Animal {
public:
    int legs;
};

class Dog : public Animal {
public:
    Dog(int n) {
        legs = n;
    }
    ~Dog() {
    }
    int bark() {
        return legs;
    }
};

int main() {
    bool flag;
    flag = true;
    const int limit = 10;

    int *p;
    p = new int;
    delete p;

    int arr[5];
    int sz;
    sz = sizeof(arr);
    int sz2;
    sz2 = sizeof(int);

    Dog d;          /* class name used directly, no `class` keyword needed */
    d.legs = 4;
    int legs;
    legs = d.bark();

    return 0;
}
