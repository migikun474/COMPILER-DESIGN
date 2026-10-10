/* t26 -- declarations: typedef, sizeof, const, struct layout, nested
   initializers, designators, multi-dimensional and string arrays,
   macros from the preprocessor */
#include <stdio.h>

#define COUNT 4
#define SQUARE(v) ((v) * (v))
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#ifdef UNDEFINED_FLAG
#define MODE 1
#else
#define MODE 2
#endif

typedef int Number;
typedef Number Row[COUNT];
typedef struct { char tag; double weight; short count; } Item;
typedef struct { Item first; Item rest[2]; int total; } Box;
struct Mixed { char a; int b; char c; short d; double e; char f; };

const int primes[COUNT] = {2, 3, 5, 7};
int matrix[2][3] = {{1, 2, 3}, {4, 5, 6}};
char letters[] = {'o', 'k', 0};
Item stock = {'s', 2.5, 3};
double table[3] = {[2] = 9.5, [0] = 1.5};

int sum(const Row r) { int s = 0; for (int i = 0; i < COUNT; i++) s += r[i]; return s; }

int main() {
    Row r = {SQUARE(2), MAX(3, 9), MODE, COUNT};
    Number n = sum(r) + sum(primes);
    printf("%d %d %d\n", n, SQUARE(1 + 2), MAX(n, 100));
    printf("%d %d %d %d\n", (int) sizeof(Item), (int) sizeof(Box), (int) sizeof(struct Mixed), (int) sizeof(Row));
    printf("%d %d %d\n", (int) sizeof(matrix), (int) (sizeof(matrix) / sizeof(matrix[0])), (int) sizeof(letters));

    Box box = {{'a', 1.5, 2}, {{'b', 2.5, 4}, {.count = 8, .tag = 'c'}}, 0};
    box.total = box.first.count + box.rest[0].count + box.rest[1].count;
    Item *it = &box.rest[1];
    it->weight = box.rest[0].weight * 2;
    printf("%d %.1f %c %.1f\n", box.total, it->weight, box.rest[1].tag, stock.weight * stock.count);

    struct Mixed m = {'x', 1, 'y', 2, 3.5, 'z'};
    struct Mixed copy = m;
    copy.b = 100;
    printf("%c %d %c %d %.1f %c %d\n", m.a, m.b, m.c, m.d, m.e, m.f, copy.b);
    printf("%s %.1f %.1f %.1f %d\n", letters, table[0], table[1], table[2], matrix[1][2] - matrix[0][0]);

    int grid[3][COUNT] = {{1}, {0, 2}, {0, 0, 3}};
    int trace = 0;
    for (int i = 0; i < 3; i++) trace += grid[i][i];
    const char *words[] = {"one", "two", "three"};
    char rows[2][6] = {"ab", "cde"};
    printf("%d %s %c %s %d\n", trace, words[2], rows[1][2], rows[0], (int) (sizeof(words) / sizeof(words[0])));
    int sensor = 5;
    int fast = sensor * 2;
    static int kept = 3;
    auto deduced = fast + kept;
    return deduced;
}
