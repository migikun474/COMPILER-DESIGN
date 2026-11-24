/* valid: the words of the dropped features are no longer reserved.
   `FILE`, `mutable` and the file-I/O names were keywords while those
   features existed; now they are ordinary identifiers that a program may
   declare and use like any other name. (`enum` and `union` were dropped
   too; `enum` came back with D42, and `union` is a reserved word again
   that the scanner rejects, D50.) */
struct FILE { int fd; };

int fopen(int mode) { return mode + 1; }
int fclose(struct FILE *f) { return f->fd; }
int feof(int at, int size) { return at >= size; }

int main() {
    int lambda = 1;
    int closure = 2;
    int mutable = lambda + closure;
    int fread = 0, fwrite = 0, fgets = 0, fputs = 0, fprintf = 0, fscanf = 0;
    struct FILE file;
    file.fd = fopen(mutable);
    if (!feof(fread, fwrite)) fgets = fputs + fprintf + fscanf;
    return fclose(&file) + fgets;
}
