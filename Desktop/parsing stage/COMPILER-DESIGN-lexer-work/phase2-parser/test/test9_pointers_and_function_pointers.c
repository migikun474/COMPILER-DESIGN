// Test basic int pointer operations only
void modify_int(int* ptr, int value) {
    *ptr = value;
}

int read_through_pointer(int* ptr) {
    return *ptr;
}

void swap_ints(int* a, int* b) {
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;
}

void increment_value(int* ptr) {
    *ptr = *ptr + 1;
}

int add_dereferenced(int* p1, int* p2) {
    return *p1 + *p2;
}

void set_pointer(int** ptr_ptr, int* value) {
    *ptr_ptr = value;
}

// Struct pointer tests
struct Point {
    int x;
    int y;
};

void set_point(struct Point* p, int x_val, int y_val) {
    p->x = x_val;
    p->y = y_val;
}

int get_point_sum(struct Point* p) {
    return p->x + p->y;
}

int main() {
    int x;
    int y;
    int sum;
    int* ptr;
    int** ptr_to_ptr;
    struct Point pt;

    x = 10;
    y = 20;
    pt.x = 0;
    pt.y = 0;

    // Test 1: modify_int should set x to 42
    modify_int(&x, 42);
    if (x != 42) {
        return 1;
    }

    // Test 2: read_through_pointer should return 42
    y = read_through_pointer(&x);
    if (y != 42) {
        return 2;
    }

    // Test 3: swap_ints should swap x and y (100 and 200)
    x = 100;
    y = 200;
    swap_ints(&x, &y);
    if (x != 200 || y != 100) {
        return 3;
    }

    // Test 4: increment_value should increment x from 5 to 6
    x = 5;
    increment_value(&x);
    if (x != 6) {
        return 4;
    }

    // Test 5: add_dereferenced should return 30 (10 + 20)
    x = 10;
    y = 20;
    sum = add_dereferenced(&x, &y);
    if (sum != 30) {
        return 5;
    }

    // Test 6: set_pointer should make ptr point to x (999)
    x = 999;
    ptr_to_ptr = &ptr;
    set_pointer(ptr_to_ptr, &x);
    y = *ptr;
    if (y != 999) {
        return 6;
    }

    // Test 7: set_point should set pt.x = 10, pt.y = 20
    set_point(&pt, 10, 20);
    if (pt.x != 10 || pt.y != 20) {
        return 7;
    }

    // Test 8: get_point_sum should return 30 (10 + 20)
    sum = get_point_sum(&pt);
    if (sum != 30) {
        return 8;
    }

    return 0;
}