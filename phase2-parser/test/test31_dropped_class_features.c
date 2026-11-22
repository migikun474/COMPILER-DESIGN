/* test31 -- the class syntax removed by D35. 'virtual' and 'explicit' are
   still reserved, so the scanner reports them by name; destructors,
   const member functions, member initializer lists and '= 0' have no
   grammar rules left, so each is an ordinary syntax error. One per
   class, each followed by a resync anchor. */

void resync_marker() {}

/* [1] a virtual function */
class T01 { public: virtual int area() { return 0; } };
int resync_after_1;

/* [2] an explicit constructor */
class T02 { public: explicit T02() { } };
int resync_after_2;

/* [3] a destructor */
class T03 { public: ~T03() { } };
int resync_after_3;

/* [4] an out-of-class destructor */
class T04 { public: int x; };
T04::~T04() { }
int resync_after_4;

/* [5] a const member function */
class T05 { public: int x; int get() const { return x; } };
int resync_after_5;

/* [6] a member initializer list */
class T06 { public: int x; T06() : x(1) { } };
int resync_after_6;

/* [7] a pure virtual function written without 'virtual' */
class T07 { public: int area() = 0; };
int resync_after_7;

int main() { return 0; }
