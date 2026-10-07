/* valid: the words of the dropped features are no longer reserved.
   `enum`, `union`, `FILE`, `mutable` and the file-I/O names were keywords
   while those features existed; now they are ordinary identifiers that a
   program may declare and use like any other name. */
struct FILE { int fd; };

int fopen(int mode) { return mode + 1; }
int fclose(struct FILE *f) { return f->fd; }
int feof(int at, int size) { return at >= size; }

int main() {
    int enum = 1;
    int union = 2;
    int mutable = enum + union;
    int fread = 0, fwrite = 0, fgets = 0, fputs = 0, fprintf = 0, fscanf = 0;
    struct FILE file;
    file.fd = fopen(mutable);
    if (!feof(fread, fwrite)) fgets = fputs + fprintf + fscanf;
    return fclose(&file) + fgets;
}
