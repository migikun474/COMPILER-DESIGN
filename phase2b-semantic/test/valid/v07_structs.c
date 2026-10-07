/* valid: structures, nested structures, typedef'd structs,
   self-referential structures, struct initializers [test 23] */
struct Point {
    int x;
    int y;
};

struct Student {
    int age;
    char grade;
    struct Point home;            /* nested structure */
};

struct Node {
    int value;
    struct Node *next;            /* pointer to the struct being defined */
};

typedef struct Point PointT;

int length(struct Node *head) {
    int n = 0;
    while (head) {
        n++;
        head = head->next;
    }
    return n;
}

struct Point make(int x, int y) {
    struct Point p = {x, y};
    return p;
}

int main() {
    struct Student s;
    s.age = 20;
    s.grade = 'A';
    s.home.x = 1;
    s.home.y = s.home.x + 1;
    struct Student *sp = &s;
    sp->age = sp->age + 1;
    sp->home.y = 3;
    struct Point a = make(1, 2);
    struct Point b;
    b = a;                        /* struct assignment */
    PointT c = {5, 6};            /* typedef'd struct: members still resolve */
    c.x = b.y;
    struct Node n1, n2;
    n1.next = &n2;
    n2.next = 0;
    struct Point pts[3];
    pts[0].x = 1;
    (&pts[1])->y = 2;
    return s.age + length(&n1) + c.x + pts[0].x + make(3, 4).y;
}
