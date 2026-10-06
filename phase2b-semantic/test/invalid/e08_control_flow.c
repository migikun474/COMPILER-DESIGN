/* invalid control flow [tests 25, 26, 29, 30] */
struct S { int v; };

void outside() {
    break;                        // error: 'break' statement not within a loop or switch
    continue;                     // error: 'continue' statement not within a loop
    case 1: ;                     // error: 'case' label not within a switch statement
    default: ;                    // error: 'default' label not within a switch statement
}

int main() {
    int x = 2;
    double d = 1.0;
    struct S s;
    int *p = &x;
    switch (x) {
        case 1: break;
        case 1: break;            // error: duplicate case value '1' (previously used at line 17)
        case 2 - 1: break;        // error: duplicate case value '1'
        case x: break;            // error: case label does not reduce to an integer constant
        default: break;
        default: break;           // error: multiple default labels in one switch
    }
    switch (x) {
        case 3:
            continue;             // error: 'continue' statement not within a loop
    }
    switch (d) { default: break; }   // error: switch quantity must have an integer type, not 'double'
    switch (p) { default: break; }   // error: switch quantity must have an integer type
    if (s) x = 1;                 // error: condition of 'if' must have a scalar
    while (s) { }                 // error: condition of 'while' must have a scalar
    for (; s; ) { }               // error: condition of 'for' must have a scalar
    do { } while (s);             // error: condition of 'do-while' must have a scalar
    until (s) { }                 // error: condition of 'until' must have a scalar
    goto nowhere;                 // error: use of undeclared label 'nowhere'
twice:
    x++;
twice:                            // error: redefinition of label 'twice'
    while (x) {
        auto inner = [&]() { break; };   // error: 'break' statement not within a loop or switch
        break;
    }
    return x;
}

int other() {
    goto twice;                   // error: use of undeclared label 'twice' (labels are local to their function)
    return 0;
}
