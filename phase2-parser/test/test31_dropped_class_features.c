/* test31 -- the class syntax removed by D35. 'explicit' is still
   reserved, so the scanner reports it by name; destructors, const member
   functions and member initializer lists have no grammar rules left, so
   each is an ordinary syntax error; '= 0' is only allowed on a virtual
   function. (Virtual functions themselves came back with D44 -- see
   phase3-ir/test/t37_virtual.c.) One per class, each followed by a resync
   anchor. */

void resync_marker() {}

/* [1] an explicit constructor */
class T01 { public: explicit T01() { } };
int resync_after_1;

/* [2] a destructor */
class T02 { public: ~T02() { } };
int resync_after_2;

/* [3] an out-of-class destructor */
class T03 { public: int x; };
T03::~T03() { }
int resync_after_3;

/* [4] a const member function */
class T04 { public: int x; int get() const { return x; } };
int resync_after_4;

/* [5] a member initializer list */
class T05 { public: int x; T05() : x(1) { } };
int resync_after_5;

/* [6] a pure virtual function written without 'virtual' */
class T06 { public: int area() = 0; };
int resync_after_6;

int main() { return 0; }
