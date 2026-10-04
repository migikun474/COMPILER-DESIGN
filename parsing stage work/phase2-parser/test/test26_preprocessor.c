/* test26 -- the preprocessor, which runs before lexing: object-like and
   function-like macros, # and ##, variadic macros, #if / #elif / #else /
   #ifdef, defined, #include of a local header (twice, stopped by its
   include guard) and of a standard header (accepted and ignored: printf
   and friends are keywords here), and __LINE__. A fully valid program;
   every line keeps its line number after preprocessing. */
#include <stdio.h>
#include "headers/geometry.h"
#include "headers/geometry.h"
#define PI 3
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define SQUARE(x) ((x) * (x))
#define STR(x) #x
#define CAT(a, b) a ## b
#define LOG(fmt, ...) printf(fmt, __VA_ARGS__)
#define NEG -1
#define DEBUG 1
#if DEBUG && defined(PI) && PI * 2 == 6
int debugOn = 1;
#elif 0
int debugOn = 2;
#else
int debugOn = 3;
#endif
#ifdef NOT_DEFINED
this line is skipped entirely
#endif
int area(int w, int h) { return w * h; }
int main() {
    int CAT(my, var) = MAX(PI, 2) + SQUARE(PI + 1);
    int x = -NEG;
    char *s = STR(hello world);
    LOG("%d %d\n", x, myvar);
    int line = __LINE__;
    int a[PI];
    return a[0] + area(SIDES, 2) + line + debugOn + s[0];
}
