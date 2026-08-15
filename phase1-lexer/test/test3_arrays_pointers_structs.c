struct Point {
    int x;
    int y;
};

enum Color {
    RED,
    GREEN,
    BLUE
};

union Data {
    int i;
    float f;
    char str[20];
};

typedef struct Point Point2D;

int main() {
    int nums[10];
    char letters[26];
    int grid[4][4];
    int cube[2][2][2];

    int *p;
    int **pp;
    int ***ppp;

    struct Point origin;
    struct Point *ptr;
    enum Color favorite;
    union Data data;

    nums[0] = 1;
    letters[0] = 'a';
    grid[1][2] = 5;
    cube[0][1][1] = 9;

    p = &nums[0];
    pp = &p;
    ppp = &pp;

    origin.x = 0;
    origin.y = 0;
    ptr = &origin;
    ptr->x = 3;
    ptr->y = 4;

    favorite = GREEN;
    data.i = 5;

    printf("%d %d\n", ptr->x, ptr->y);
    scanf("%d", &nums[1]);

    return 0;
}
