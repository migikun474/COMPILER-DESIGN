/* test19 -- syntax errors in struct/class declarations: malformed
   bodies, bad member lists, bad inheritance lists, and access
   specifiers used somewhere they can't be. One broken construct per
   top-level declaration. */

void resync_marker() {}

/* [1] struct missing the closing '}' before its ';' */
struct T01_Point {
    int x;
    int y;
;

/* [2] struct member missing its own ';' */
struct T02_Line {
    int x1
    int y1;
};

/* [3] struct member list with a missing comma between declarators */
struct T03_Color { int red, green blue; };

/* [4] class with a member missing its own ';' */
class T04_Value {
    int i
    float f;
};

/* [5] class with a bad inheritance list -- ':' with no base name */
class T05_Bad : {
    int a;
};

/* [6] class inheriting with an access specifier but no base name */
class T06_Bad2 : public {
    int a;
};
int resync_after_6;

/* [7] a bare access specifier at file scope -- 'public:' only means
   anything inside a class/struct body, not here */
public:
int t07_after_bad_access_specifier;

/* [8] constructor-looking definition with a missing ')' */
class T08_Widget {
public:
    T08_Widget(int w, int h {
        resync_marker();
    }
};

/* [9] destructor with a missing identifier after '~' */
class T09_Gadget {
public:
    ~() {
        resync_marker();
    }
};

/* a fully valid struct/class pair proving the parser recovered after
   all nine broken aggregate declarations above */
struct T10_Ok {
    int a;
    int b;
};

class T11_Ok {
public:
    T11_Ok(int v) {
        resync_marker();
    }
private:
    int v;
};

int main() {
    struct T10_Ok p;
    p.a = 1;
    p.b = 2;
    return p.a + p.b;
}
