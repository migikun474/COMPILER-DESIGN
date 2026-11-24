/* invalid: 'explicit' is still a reserved word, but the language has no
   converting constructors (D35); the scanner reports it and the rest of
   the file is not analyzed. ('virtual' was reserved the same way until
   virtual functions came back with D44.) */
class Shape {
public:
    int id;
    explicit Shape() { }                      // error: 'explicit' is not supported: this language has no converting constructors
};
int main() {
    return 0;
}
