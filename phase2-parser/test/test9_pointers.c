
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
    int nums[3];
    int (*row)[3];
    row = &nums;
    (*row)[0] = 1;
    int result;
    result = add(2, (*row)[0]);

    int *val;
    val = makeInt();

    int x;
    x = argc;

    return 0;
}
