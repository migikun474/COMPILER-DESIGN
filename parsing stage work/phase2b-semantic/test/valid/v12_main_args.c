/* valid: command-line input */
int main(int argc, char **argv) {
    int i;
    for (i = 1; i < argc; i++) {
        printf("%s\n", argv[i]);
        char first = argv[i][0];
        if (first == '-') printf("option %c\n", argv[i][1]);
    }
    return argc > 1 ? 0 : 1;
}
