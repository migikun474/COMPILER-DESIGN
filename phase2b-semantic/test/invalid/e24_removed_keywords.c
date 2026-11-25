/* invalid: 'virtual', 'explicit', 'union' and the va_* words are still
   reserved, but the language no longer has virtual functions, converting
   constructors (D35), unions (D50) or variable-argument functions (D51);
   the scanner reports them and the rest of the file is not analyzed
   ('...' is a syntax error, shown by ../phase2-parser/test/test17) */
class Shape {
public:
    virtual int area() { return 0; }          // error: 'virtual' is not supported: this language has no virtual functions
    explicit Shape() { }                      // error: 'explicit' is not supported: this language has no converting constructors
};
va_list args;                                  // error: 'va_list' is not supported: this language has no variable-argument functions
union Value { int i; float f; };              // error: 'union' is not supported: this language has no unions
int main() {
    return 0;
}
