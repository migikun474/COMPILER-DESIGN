#include <stdio.h>
#define PI 3
#define AREA(r) (PI * (r) * (r))
#ifdef PI
int area = AREA(2);
#else
int area = 0;
#endif
