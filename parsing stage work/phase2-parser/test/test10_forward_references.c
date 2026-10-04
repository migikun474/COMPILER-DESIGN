

int main() {
    goto done;
    int x;
    x = 1;
done:
    return add(1, 2);
}

int add(int a, int b) {
    return a + b;
}
