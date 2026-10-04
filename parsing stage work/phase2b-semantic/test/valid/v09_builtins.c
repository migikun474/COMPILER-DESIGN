/* valid: printf/scanf, dynamic memory and file I/O builtins */
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

    FILE *f = fopen("data.txt", "w");
    fprintf(f, "%d\n", x);
    fputs("line\n", f);
    fclose(f);
    f = fopen("data.txt", "r");
    fscanf(f, "%d", &x);
    if (fgets(buf, 32, f)) x++;
    int items = fread(buf, 1, 32, f) + fwrite(buf, 1, 4, f);
    while (!feof(f)) break;
    fclose(f);
    return items;
}
