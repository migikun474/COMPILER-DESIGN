/* invalid: preprocessor errors (they stop compilation before semantic analysis) */
#define PI 3
#define PI 4                    // warning: 'PI' macro redefined
#define TWO(a, b) a + b
#include "missing.h"            // error: 'missing.h' file not found
#include <graphics.h>           // error: 'graphics.h' file not found
#frobnicate                     // error: invalid preprocessing directive '#frobnicate'
#else                           // error: #else without #if
#if 1 +                         // error: invalid #if expression
#endif
#if 0
#anything-goes-in-a-skipped-group
#endif
#define 5 five                  // error: macro name must be an identifier
#define BAD(x) #y               // error: '#' is not followed by a macro parameter
#error stop right here          // error: #error stop right here
int main() { return TWO(1); }   // error: macro 'TWO' requires 2 arguments, but 1 was given
#ifdef PI                       // error: unterminated conditional directive
