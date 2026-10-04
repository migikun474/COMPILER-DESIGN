/* valid: `char *argv[]` is the same parameter type as `char **argv` */
int main(int argc, char *argv[]) {
    return argv[argc - 1][0];
}
