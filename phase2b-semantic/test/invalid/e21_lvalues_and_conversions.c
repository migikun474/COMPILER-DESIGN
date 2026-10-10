/* invalid: the other side of v25 */
typedef int Row[4];
int first(const Row r) {
    r[0] = 1;                     // error: cannot assign
    return r[0];
}
int write(Row r) { return r[0]; }
const int primes[4] = {2, 3, 5, 7};

int main() {
    int x = 1;
    const int c = 2;
    double d = 3.0;
    (x ? x : c) = 5;              // error: not assignable
    (x ? x : d) = 5;              // error: not assignable
    int &r = x ? x : d;           // error: cannot bind to a temporary
    int *p = &(x ? x : 3);        // error: cannot take the address of an rvalue
    return write(primes);         // error: conversion discards 'const' qualifier
}
