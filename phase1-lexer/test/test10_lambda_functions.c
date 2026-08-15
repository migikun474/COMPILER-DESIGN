/* Lambda functions use C++-style syntax: [capture](params) { body }
 * No new tokens were needed for this -- every piece decomposes into
 * tokens the lexer already had: [ ], ( ), { }, ->, and existing
 * operators/identifiers inside the capture list. The one real gap this
 * exposed was 'auto' not being a keyword -- fixed alongside this test,
 * since a lambda's value needs somewhere to be assigned.
 */

int main() {
    auto add = [](int x, int y) {
        return x + y;
    };

    auto byRef = [&](int x) {
        return x + 1;
    };

    auto byValue = [=](int x) {
        return x + 1;
    };

    int a = 1;
    int b = 2;
    auto mixedCapture = [a, &b](int z) {
        return a + b + z;
    };

    auto withReturnType = [](int x) -> int {
        return x * 2;
    };

    return 0;
}
