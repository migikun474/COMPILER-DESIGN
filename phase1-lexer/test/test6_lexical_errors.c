int main() {
    int x = 12abc;
    char bad = 'a;
    char *s = "oops;
    int y = 5 @ 3;
    float f = 3.14x;
    char multi = 'AB';
    char badesc = '\q';
    char *badhex = "\xz";
    char *badoct = "\89";
    int badoctnum = 089;
    int badsuffix = 45lL;
    /* this comment never closes
    int z = 1;
