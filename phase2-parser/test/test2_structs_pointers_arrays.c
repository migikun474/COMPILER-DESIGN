typedef int MyInt;

struct Point {
    int x;
    int y;
};

int add(int a, int b) {
    return a + b;
}

int main() {
    struct Point p;
    MyInt x = 5;
    int *ptr;
    int arr[10];
    ptr = &x;
    p.x = 1;
    for (int i = 0; i < 10; i++) {
        arr[i] = i;
    }
    if (x > 0) {
        printf("positive\n");
    } else {
        printf("non-positive\n");
    }
    while (x > 0) {
        x = x - 1;
    }
    switch (x) {
        case 0:
            break;
        default:
            break;
    }
    int result = add(x, *ptr);
    return 0;
}
