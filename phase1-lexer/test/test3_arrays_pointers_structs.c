struct Point {
    int x;
    int y;
};

enum Color {
    RED,
    GREEN,
    BLUE
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

    printf("%d %d\n", ptr->x, ptr->y);
    scanf("%d", &nums[1]);

    return 0;
}
