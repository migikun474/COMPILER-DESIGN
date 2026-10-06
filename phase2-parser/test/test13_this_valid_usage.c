

class Dog {
public:
    int legs;
    int bark() {
        return this->legs;
    }
    int legCount();
};

int Dog::legCount() {
    return this->legs;
}

int main() {
    return 0;
}
