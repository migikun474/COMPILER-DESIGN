
int add(int a, int b) {
    return a + b;
}

int *makeInt() {
    int *p;
    p = new int;
    *p = 42;
    return p;
}

int main(int argc, char **argv) {
    int (*fp)(int, int);
    fp = add;
    int result;
    result = fp(2, 3);

    int *val;
    val = makeInt();

    int x;
    x = argc;

    return 0;
}
