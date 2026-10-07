/* valid: printf/scanf and dynamic memory builtins */
int main() {
    int x = 0, n = 3;
    char buf[32];
    double d = 1.5;
    printf("%d %s %c %5.2f %% %x\n", x, "str", 'c', d, x);
    printf("no arguments\n");
    printf("%*d\n", 5, x);
    scanf("%d", &x);
    scanf("%31s", buf);           /* an array decays to the pointer scanf needs */
    scanf("%d %lf", &n, &d);

    int *heap = (int *) malloc(n * sizeof(int));
    heap[0] = 42;
    int *zeroed = (int *) calloc(n, sizeof(int));
    zeroed = (int *) realloc(zeroed, 2 * n * sizeof(int));
    char *text = malloc(16);      /* void * converts to any object pointer */
    free(heap);
    free(zeroed);
    free(text);
    return x + n;
}
