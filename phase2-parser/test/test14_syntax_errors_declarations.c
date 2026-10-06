/* test14 -- syntax errors in declarations, initializers and bare
   top-level statements. Each broken block is separated by a fully
   valid declaration so panic-mode recovery ends cleanly before the
   next block starts (a clean re-sync point) -- this isolates one
   error per block instead of letting one broken construct's recovery
   swallow the next. See test21 for what happens WITHOUT that
   isolation (dense clusters of back-to-back errors).

   NOTE: this grammar performs no semantic checks and no extra
   syntax-shape checks beyond what the productions themselves accept --
   every rule below is either accepted purely because some production
   matches it, or rejected purely because none does. Three cases
   below (marked [boundary]) look like they should be errors but
   aren't, precisely because of that: the grammar has a production
   that matches them even though the result declares nothing useful. */

int resync0 = 0;

/* [1] missing ';' between two declarations */
int a
int b;
int resync1 = 1;

/* [boundary] `int;` alone -- declaration_specifiers init_declarator_
   list_opt ';' matches this with init_declarator_list_opt empty, so
   it's a VALID reduction, not a syntax error, even though it declares
   nothing. (Real g++ special-cases this and rejects it; this grammar
   doesn't add that check, so it stays purely production-driven.) */
int;
int resync2 = 2;

/* [boundary] same story for a bare storage-class keyword */
static;
int resync3 = 3;

/* [2] missing initializer expression after '=' */
int c = ;
int resync4 = 4;

/* [3] unknown type name used as if it were a type (no typedef/struct
   for "Whatsit" exists anywhere) -- two bare identifiers in a row */
Whatsit d;
int resync5 = 5;

/* [4] trailing comma with nothing after it in a declarator list */
int e, ;
int resync6 = 6;

/* [boundary] `typedef int;` -- same shape as the two boundary cases
   above: declaration_specifiers (TYPEDEF, INT) + empty declarator
   list + ';' is a valid reduction on its own terms. */
typedef int;
int resync7 = 7;

/* [5] unterminated initializer list -- missing closing '}' */
int arr1[3] = {1, 2, 3;
int resync8 = 8;

/* [6] initializer list with a stray extra comma before the value */
int arr2[3] = {1, , 3};
int resync9 = 9;

/* [7] a bare expression statement at file scope -- not a declaration,
   not a function definition, so it can't appear here at all */
global_undeclared_but_thats_not_the_point = 2;
int resync10 = 10;

int main() {
    /* [8] double pointer assigned to a missing operand for '&' */
    int *p = &;
    int resync11 = 11;

    /* [9] multi-dimensional array missing the second ']' */
    int m[2][3;
    int resync12 = 12;

    /* [10] cast with an incomplete type name */
    int y = (int ;
    int resync13 = 13;

    return 0;
}
