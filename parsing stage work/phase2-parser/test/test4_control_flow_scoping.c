

int sum_to(int n) {
    int total;
    total = 0;
    for (int i = 1; i <= n; i = i + 1) {
        total = total + i;
    }
    return total;
}

int classify(int n) {
    switch (n) {
        case 0:
            return 0;
        case 1:
            return 1;
        default:
            break;
    }
    return -1;
}

int main() {
    int n;
    n = 5;
    int s;
    s = sum_to(n);
    int c;
    c = classify(n);
    printf("%d %d\n", s, c);
    return 0;
}
