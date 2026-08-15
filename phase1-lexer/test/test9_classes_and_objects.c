/* Covers this language's object-oriented keywords/operators:
 *  - class
 *  - access modifiers: public, private, protected
 *  - this (self-reference inside a method)
 *  - :: (scope resolution)
 */

class Animal {
    public:
        int age;

        void setAge(int a) {
            this->age = a;
        }

        int getAge() {
            return this->age;
        }

    private:
        int secretId;

    protected:
        int sharedValue;
};

class Dog {
    public:
        Animal base;

        void bark() {
            this->base.age = 1;
        }
};

int main() {
    Animal a;
    a.setAge(5);

    Dog d;
    d.bark();

    Animal::setAge;

    return 0;
}
