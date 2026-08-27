int main() {
    char bad = 'a;
    char *s = "oops;
    int y = 5 @ 3;
    char multi = 'AB';
    char badesc = '\q';
    char *badhex = "\xz";
    char *badoct = "\89";
    int badoctnum = 089;
    int badbinnum = 0b1102;
    int barehex = 0x;
    int barebin = 0b;
    /* this comment never closes
    int z = 1;
