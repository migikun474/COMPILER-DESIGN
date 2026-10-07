/* t11 -- command-line arguments (run with: alpha beta) */
#include <stdio.h>

int main(int argc, char **argv) {
    int letters = 0;
    for (int i = 1; i < argc; i++) {
        char *s = argv[i];
        while (*s) { letters++; s++; }
        printf("%d: %s\n", i, argv[i]);
    }
    printf("%d %d\n", argc, letters);
    return argc;
}
