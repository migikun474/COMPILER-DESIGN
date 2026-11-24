/* invalid: 'virtual', 'explicit' and 'union' are still reserved words,
   but the language no longer has virtual functions, converting
   constructors (D35) or unions (D50); the scanner reports them and the
   rest of the file is not analyzed */
class Shape {
public:
    virtual int area() { return 0; }          // error: 'virtual' is not supported: this language has no virtual functions
    explicit Shape() { }                      // error: 'explicit' is not supported: this language has no converting constructors
};
union Value { int i; float f; };              // error: 'union' is not supported: this language has no unions
int main() {
    return 0;
}
