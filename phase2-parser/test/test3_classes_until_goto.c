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
    class Shape s;
    s.sides = 4;

    int x = 5;
    int y = 10;
    auto total = x + y + s.area();

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
