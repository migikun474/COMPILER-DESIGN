/* invalid: the other side of v26 */
class Shape { public: int sides() { return 0; } };
class Square : public Shape { public: int sides() { return 4; } };
class Other { public: int sides() { return 9; } int extra; };

int main() {
    Square q;
    Square *p = &q;
    int a = q.Other::sides();     // error: is not
    int b = p->Other::extra;      // error: is not
    int c = q.Shape::missing;     // error: no member named 'missing'
    return a + b + c;
}
