/* valid: if/else, loops, break/continue, switch, goto, until
   [test 27, 28, 31, 32] */
const int RED = 0, GREEN = 5, BLUE = 6;

int classify(int c) {
    switch (c) {
        case RED: return 0;
        case GREEN: return 1;
        case BLUE:                /* falls through */
        default: break;
    }
    return -1;
}

int main() {
    int i, total = 0;
    for (i = 0; i < 10; i++) {
        if (i == 2) continue;     /* valid continue */
        if (i == 8) break;        /* valid break */
        total += i;
    }
    while (total > 100) total--;
    do { total++; } while (total < 5);
    until (total >= 50) { total += 7; }
    switch (total) {
        case 1: case 2: total = 0; break;
        case 'A': total = 65; break;
        case 3 + 4: total = 7; break;     /* constant expressions are fine */
        default: total = -total;
    }
    for (;;) {
        switch (i) {
            case 0: continue;     /* continue inside switch inside loop */
            default: break;       /* breaks the switch only */
        }
        break;                    /* breaks the loop */
    }
    goto end;                     /* forward goto */
again:
    total++;
    if (total < 3) goto again;    /* backward goto */
end:
    if (total) total = classify(BLUE); else total = classify(RED);
    return total;
}
