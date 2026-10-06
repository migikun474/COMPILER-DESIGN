/* valid: nested scopes, shadowing, global/local name collisions
   [test 8, 9, 33, 34] */
int x = 1;
int y = 2;

int shadow(int y) {               /* parameter shadows the global y */
    int x = y * 2;                /* local shadows the global x */
    {
        char x = 'q';             /* inner block shadows the local x */
        y = x;
    }
    return x + y;
}

int x_func() { return x; }        /* the global x again */

int main() {
    int total = x;
    {
        int total2 = total + 1;
        {
            int total3 = total2 + 1;
            {
                double x = 0.5;   /* four levels deep, shadowing the global */
                total = total3 + x;
            }
        }
    }
    for (int i = 0; i < 3; i++) {
        int x = i;                /* new x every iteration */
        total += x;
    }
    for (int i = 0; i < 2; i++) { total += i; }   /* `i` can be declared again */
    int y = shadow(total);        /* a local named like a global */
    return total + y + x_func();
}
