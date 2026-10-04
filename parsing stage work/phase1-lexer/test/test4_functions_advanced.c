typedef int MyInt;

int add(int a, int b) {
    return a + b;
}

int sum(int count, ...) {
    int total = 0;
    return total;
}

void increment(int &value) {
    value = value + 1;
}

int main(int argc, char **argv) {
    MyInt x = 5;
    MyInt y = 10;
    int z = add(x, y);

    int total = sum(3, 1, 2, 3);

    int *heap = (int *) malloc(10 * sizeof(int));
    heap[0] = 42;
    free(heap);

    increment(z);

    if (argc > 1) {
        printf("%s\n", argv[1]);
    }

    return 0;
}
