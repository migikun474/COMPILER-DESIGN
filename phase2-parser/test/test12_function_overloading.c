

int add(int a, int b) {
    return a + b;
}
int add(int a, int b, int c) {
    return a + b + c;
}

int combine(int a, int b) {
    return a + b;
}
int combine(char a, char b) {
    return a + b;
}

int main() {
    int r1;
    r1 = add(1, 2);
    int r2;
    r2 = add(1, 2, 3);

    int r3;
    r3 = combine(1, 2);
    char x;
    char y;
    int r4;
    r4 = combine(x, y);

    return 0;
}
