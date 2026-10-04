enum Color { RED, GREEN, BLUE };

class Shape {
public:
    int sides;
    int area() {
        return sides * sides;
    }
private:
    int secret;
};

int main() {
    enum Color c;
    c = RED;
    class Shape s;
    s.sides = 4;

    int (*fp)(int, int);

    int x = 5;
    int y = 10;
    auto adder = [x, &y](int z) {
        return x + y + z;
    };

    until (x <= 0) {
        x = x - 1;
    }

    do {
        x++;
    } while (x < 5);

    goto done;
done:
    return 0;
}
