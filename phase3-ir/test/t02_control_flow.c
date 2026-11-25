/* t02 -- control flow: if/else chains, while, do-while, for with a
   declaration, until (plain, never entered, with break and continue, a
   compound condition, nested), switch with fall-through and default in
   the middle, break/continue, goto out of two loops, a state machine.
   Expected: g++ -include test/gpp_prelude.h (it defines until). */
int kind(char c) {                     /* 0 other, 1 digit, 2 letter */
    if (c >= '0' && c <= '9') return 1;
    else if ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z')) return 2;
    else return 0;
}
int main() {
    int s = 0, i = 0;
    while (i < 5) s += i++;
    do s *= 2; while (s < 100);
    for (int k = 0; k < 3; k++) s -= k;
    for (i = 0; i < 4; i++) ;                  /* an empty body */
    int u = 0;
    until (u >= 4) u++;
    printf("%d %d\n", s, u);
    int never = 0, steps = 0, odd = 0, cells = 0, rows = 0;
    until (1) never++;                         /* the condition holds at once: no iteration */
    until (steps == 10) {
        steps++;
        if (steps % 2 == 0) continue;
        if (steps > 7) break;
        odd += steps;
    }
    until (rows >= 3 || cells > 4) {           /* a compound condition */
        int c = 0;
        until (c == rows + 1) { cells++; c++; } /* nested */
        rows++;
    }
    printf("%d %d %d %d %d\n", never, steps, odd, rows, cells);
    int out = 0;
    for (i = 0; i < 6; i++) {
        switch (i) {
            case 0: case 1: out += 1;
            default: out += 10; break;
            case 4: out += 100;
            case 5: out += 1000; continue;
        }
        out += 5;
    }
    printf("%d\n", out);
    int r, c = 0, hit = 0;
    for (r = 0; r < 4; r++)
        for (c = 0; c < 4; c++) {
            if (c > r) break;
            if ((r + c) % 2) continue;
            if (r * c == 4) goto done;
            hit++;
        }
done:
    printf("%d %d %d\n", hit, r, c);
    const char *text = "ab 12 x9;";
    int state = 0, words = 0;
    for (i = 0; text[i]; i++) {
        int k = kind(text[i]);
        if (state == 0 && k) { words++; state = 1; }
        else if (state == 1 && !k) state = 0;
    }
    printf("%d\n", words);
    return 0;
}
