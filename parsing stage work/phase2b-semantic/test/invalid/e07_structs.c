/* invalid structures [test 24: invalid structure member] */
struct Student {
    int age;
    char grade;
};

struct Dup {
    int a;
    char a;                       // error: duplicate member 'a' in struct 'Dup'
};

struct Self {
    struct Self inner;            // error: field 'inner' has incomplete type 'struct Self'
};

union U { int i; };
struct Other { int age; };

int main() {
    struct Student s;
    struct Student *sp = &s;
    struct Other o;
    int n = 0;
    s.name = 1;                   // error: no member named 'name' in 'struct Student'
    n = sp.age;                   // error: is a pointer; did you mean to use '->'?
    n = s->age;                   // error: is not a pointer; did you mean to use '.'?
    n = n.age;                    // error: member reference base type 'int' is not a struct
    s = o;                        // error: cannot assign 'struct Other' to 'struct Student'
    s.age = "old";                // error: cannot assign 'char *' to 'int'
    struct Student t = {1, 'a', 3};   // error: excess elements in struct initializer
    union U u = {1, 2};           // error: excess elements in union initializer
    struct U wrong;               // error: tag type 'struct' that does not match its declaration as 'union'
    return s.age;
}
