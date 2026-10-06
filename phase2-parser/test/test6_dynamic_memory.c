

int main() {
    int *heap;
    heap = (int *) malloc(10 * 4);
    heap[0] = 42;
    free(heap);

    int *more;
    more = (int *) calloc(5, 4);
    more = (int *) realloc(more, 20);
    free(more);

    return 0;
}
