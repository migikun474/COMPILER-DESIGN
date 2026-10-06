/* test23 -- syntax errors around forward references and scope
   resolution: goto/label forward references, calling a function
   defined later in the file, out-of-class method definitions
   (`Dog::bark() {...}`), and the `::` scope-resolution operator used
   in an expression. These are the features documented in
   `test10_forward_references.c` and `test8_out_of_class_methods.c` --
   this file is their broken-syntax counterpart, same one-construct-
   per-function discipline as test14-test22.

   Also includes two deliberate NON-error "boundary" cases at the end
   (clearly marked, not counted among the errors) -- one obvious
   (referencing a struct tag that's never defined is fine, it's just
   a forward declaration use) and one genuinely surprising (leaving
   the '::' off an out-of-class method with a correctly-spelled class
   name doesn't error at all; it silently parses as an unrelated free
   function). Both were found by testing, not assumed. */

void resync_marker() {}

/* [1] goto with a target label but a missing ';' */
void t01_goto_missing_semicolon() {
    goto later
later:
    resync_marker();
}

/* [2] goto with a keyword instead of a label identifier */
void t02_goto_target_is_a_keyword() {
    goto int;
}

/* [3] a label definition missing its ':' */
void t03_label_missing_colon() {
    int a = 1;
    goto skip;
skip
    a = a + 1;
}

/* [4] forward call to a not-yet-defined function, but with the call
   itself malformed (missing closing paren) -- forward resolution
   should not mask an otherwise-ordinary syntax error */
void t04_forward_call_missing_close_paren() {
    int r = later_defined_fn(1, 2;
}
int later_defined_fn(int a, int b) { return a + b; }

/* [5] out-of-class method definition whose class name is misspelled/
   undeclared -- two bare identifiers in a row (neither is a
   recognized TYPE_NAME, so declaration_specifiers has nothing to
   build on) IS a real syntax error, same shape as test14's "Whatsit
   d;" case. See the note after case [8] below for the much more
   surprising thing that happens when the class name IS spelled
   correctly but the '::' itself is just left out. */
class T05_Cat {
public:
    int feed(int amount);
};
T05_Cta feed(int amount) {
    return amount;
}

/* [6] out-of-class method definition with '::' but a missing method
   name after it */
class T06_Dog {
public:
    int bark();
};
int T06_Dog::(int volume) {
    return volume;
}

/* [7] out-of-class method definition whose body is missing its
   closing ')' on the parameter list */
class T07_Bird {
public:
    int fly(int speed);
};
int T07_Bird::fly(int speed {
    return speed;
}

/* [8] '::' used in an expression (not a declarator) with a missing
   member name after it */
class T08_Util {
public:
    static int value();
};
void t08_scope_res_expr_missing_identifier() {
    int v = T08_Util::;
}

/* [boundary A] a forward reference to a struct tag that's never
   actually defined anywhere in the file, used as a type -- STRUCT
   IDENTIFIER without a body is a valid *reference* grammatically (a
   forward declaration use), so this specific case is NOT a syntax
   error; it's included to document that boundary precisely, right
   next to the cases that ARE errors, instead of leaving it ambiguous */
struct NeverDefinedAnywhere *boundaryA_forward_tag_reference_is_fine;

/* [boundary B] the far more surprising non-error: leaving the '::'
   out of an out-of-class method definition entirely, when the class
   name IS spelled correctly and IS a recognized TYPE_NAME. Unlike
   case [5] above (a genuinely unknown name), "T11_Fish jump(...)"
   here reduces cleanly as declaration_specifiers=[INT? no --
   TYPE_NAME "T11_Fish"] declarator="jump(...)" -- an ordinary,
   syntactically valid function definition named `jump` that happens
   to have a nonsensical *return type* of `T11_Fish`. This grammar
   never checks that a return type "makes sense", so forgetting '::'
   on a correctly-spelled class name is NOT caught here at all -- it
   silently becomes a free function with a bizarre return type
   instead of the out-of-class method you meant. Genuinely useful to
   know before relying on this parser to catch that mistake. */
class T11_Fish {
public:
    int jump(int height);
};
T11_Fish jump(int height) {
    return height;
}

/* a fully valid pair proving the parser recovered after all eight
   broken constructs above -- exercises forward goto, forward function
   calls, out-of-class methods and '::' expressions correctly */
class T10_Ok {
public:
    int compute(int x);
};

int T10_Ok::compute(int x) {
    return x * 2;
}

int main() {
    goto done;
    int unused = compute_later(3);
done:
    T10_Ok obj;
    return obj.compute(unused);
}

int compute_later(int x) { return x + 1; }
