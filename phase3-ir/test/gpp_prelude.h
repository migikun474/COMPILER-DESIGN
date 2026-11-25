/* For checking the test programs with a real C/C++ compiler only:
     g++ -include test/gpp_prelude.h test/tNN_name.c
   Our language has printf, scanf, malloc ... built in and no
   preprocessor (D34), so the programs have no #include and cannot define
   macros; this header supplies both for gcc/g++. `until (c) S` is this
   language's loop that runs S while c is false. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define until(c) while (!(c))
