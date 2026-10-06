/* test21 -- deliberately DOESN'T isolate each error behind a resync
   anchor, unlike every other new test file in this suite. The point
   here is the opposite: to show what panic-mode recovery actually
   does under realistic "someone is still typing" conditions, where
   several broken constructs sit close together with nothing clean in
   between.

   Two distinct failure shapes show up, both real and both worth
   knowing about if you're relying on "every error gets reported":

   1. SILENT SWALLOWING -- one broken construct's recovery can eat one
      or more syntactically fine statements/declarations right after
      it without ever reporting them as their own error, or even
      acknowledging they were skipped. The diagnostic count under-
      reports how much of the file was actually thrown away.

   2. TOTAL ABORT -- badly-timed errors (see test16 for the clearest,
      most reproducible trigger: any malformed do-while) can make
      yyparse() give up on the rest of the file entirely. This build
      now at least surfaces that as a "fatal error" diagnostic (see
      main.cpp) instead of staying silent about it, but the underlying
      content is still gone either way.

   Compare this file's error count and AST against test14-test20 (each
   of which isolates one error at a time and gets a clean 1:1 count)
   to see the difference concretely. */

int a;
int b
int c;
int d = ;
int e, ;
int f[3] = {1, 2, 3;
int g[3] = {1, , 3};

int main() {
    int x = 1;

    if (x > 0 {
        x = x + 1;
    }

    while (x > 0 {
        x = x - 1;
    }

    for (x = 0 x < 10; x++) {
        x = x;
    }

    switch (x {
        case 1: break;
    }

    return 0;
}
