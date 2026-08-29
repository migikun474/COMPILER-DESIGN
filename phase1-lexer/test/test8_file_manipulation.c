/* Covers this language's custom file_keyword reserved words: FILE,
 * fopen, fclose, fread, fwrite, fprintf, fscanf, fgets, fputs, feof.
 * Real C treats all of these as ordinary <stdio.h> library identifiers;
 * here they are reserved keywords by design (see lexer.l header).
 */

int main() {
    FILE *fp;
    char buffer[100];
    int value;

    fp = fopen("data.txt", "r");
    if (fp) {
        fgets(buffer, 100, fp);
        fscanf(fp, "%d", &value);
        while (!feof(fp)) {
            fread(buffer, 1, 100, fp);
        }
        fclose(fp);
    }

    fp = fopen("out.txt", "w");
    fputs("hello", fp);
    fprintf(fp, "%d\n", value);
    fwrite(buffer, 1, 100, fp);
    fclose(fp);

    return 0;
}
