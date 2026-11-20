/* invalid: 'virtual' and 'explicit' are still reserved words, but the
   language no longer has virtual functions or converting constructors
   (D35); the scanner reports them and the rest of the file is not analyzed */
class Shape {
public:
    virtual int area() { return 0; }          // error: 'virtual' is not supported: this language has no virtual functions
    explicit Shape() { }                      // error: 'explicit' is not supported: this language has no converting constructors
};
int main() {
    return 0;
}
