int global;

int add(int a, int b) {
    int result;
    result = a + b;
    return result;
}

int main() {
    int x = 2;
    {
        int x = 3;          /* shadows the outer x */
        global = add(x, 4);
    }
    return global + x;
}
