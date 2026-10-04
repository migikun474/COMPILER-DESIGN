/* test22 -- syntax errors around the file-manipulation keywords:
   FILE, fopen, fclose, fread, fwrite, fprintf, fscanf, fgets, fputs,
   feof. Each of these is a reserved builtin-call token in this
   grammar (see `builtin_call` in parser.y), not an ordinary
   identifier, so it can't be reused as a variable name either --
   that misuse gets its own case here too. One broken construct per
   function, verified independently. */

void resync_marker() {}

/* [1] FILE* declarator missing its own ';' */
void t01_file_decl_missing_semicolon() {
    FILE *f
    f = fopen("data.txt", "r");
}

/* [2] fopen call missing its closing ')' */
void t02_fopen_missing_close_paren() {
    FILE *f;
    f = fopen("data.txt", "r";
}

/* [3] fopen call with a stray leading comma */
void t03_fopen_stray_leading_comma() {
    FILE *f;
    f = fopen(, "r");
}

/* [4] fclose call missing its argument list parens entirely -- FCLOSE
   is a fixed-shape builtin_call, not an ordinary function, so this is
   a hard grammar mismatch, not just "wrong arity" */
void t04_fclose_missing_parens() {
    FILE *f;
    f = fopen("data.txt", "r");
    fclose f;
}

/* [5] fread call with unbalanced parens */
void t05_fread_missing_close_paren() {
    FILE *f;
    int buf[10];
    fread(buf, 4, 10, f;
}

/* [6] fwrite call with a dangling comma before the closing paren */
void t06_fwrite_dangling_comma() {
    FILE *f;
    int buf[10];
    fwrite(buf, 4, 10, f, );
}

/* [7] fprintf call missing its closing ')' */
void t07_fprintf_missing_close_paren() {
    FILE *f;
    fprintf(f, "x = %d", 3;
}

/* [8] fscanf call with a stray leading comma */
void t08_fscanf_stray_comma() {
    FILE *f;
    int x;
    fscanf(, f, "%d", &x);
}

/* [9] fgets call missing its closing ')' */
void t09_fgets_missing_close_paren() {
    FILE *f;
    char buf[100];
    fgets(buf, 100, f;
}

/* [10] fputs call with a dangling comma */
void t10_fputs_dangling_comma() {
    FILE *f;
    fputs("hello", f, );
}

/* [11] feof used with an empty argument list left dangling by a stray
   comma */
void t11_feof_dangling_comma() {
    FILE *f;
    int done;
    done = feof(f,);
}

/* [12] FILE, fopen, fclose etc. are reserved keywords in this
   language (see phase1-lexer's README, "Deviations from Real C") --
   using one as a variable/parameter name is a hard grammar error here,
   unlike in real C where fopen/fclose/etc. are just ordinary library
   identifiers */
void t12_reserved_file_keyword_as_identifier() {
    int fopen;
    fopen = 5;
}

/* a fully valid function proving the parser recovered after all
   twelve broken file-I/O constructs above -- exercises every one of
   these builtins correctly */
int main() {
    FILE *f = fopen("data.txt", "w");
    fprintf(f, "%d\n", 42);
    fputs("hello\n", f);
    fclose(f);

    FILE *g = fopen("data.txt", "r");
    char buf[100];
    int x;
    fgets(buf, 100, g);
    fscanf(g, "%d", &x);
    fread(buf, 1, 100, g);
    fwrite(buf, 1, 100, g);
    int done = feof(g);
    fclose(g);

    return done;
}
