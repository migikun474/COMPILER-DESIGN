/* invalid: there is no preprocessor (D34); every directive is a lexical error */
#include <stdio.h>          // error: preprocessor directive '#include' is not supported
#define N 3                 // error: preprocessor directive '#define' is not supported
  #if 1                     // error: preprocessor directive '#if' is not supported
#endif                      // error: preprocessor directive '#endif' is not supported
int main() {
    printf("%d\n", 4);
    return 0;
}
