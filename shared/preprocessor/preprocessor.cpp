#include "preprocessor/preprocessor.hpp"

#include <cctype>
#include <climits>
#include <cstring>
#include <fstream>
#include <map>
#include <set>
#include <sstream>
#include <vector>

#include "diagnostics/diagnostics.hpp"

namespace {

/* ---------------- preprocessing tokens ---------------- */

struct Tok {
    enum Kind { Ident, Number, Str, Chr, Punct, Space, Comment } kind;
    std::string text;
};

bool isSpaceChar(char c) { return c == ' ' || c == '\t' || c == '\r' || c == '\f' || c == '\v'; }
bool isIdentChar(char c) { return std::isalnum(static_cast<unsigned char>(c)) || c == '_'; }

/* splits one line into pp-tokens; `inComment` carries a block comment
   that is still open at the end of a line into the next one */
std::vector<Tok> tokenize(const std::string &s, bool &inComment) {
    std::vector<Tok> out;
    size_t i = 0, n = s.size();
    if (inComment) {
        size_t e = s.find("*/");
        if (e == std::string::npos) {
            out.push_back({Tok::Comment, s});
            return out;
        }
        out.push_back({Tok::Comment, s.substr(0, e + 2)});
        i = e + 2;
        inComment = false;
    }
    static const char *multi[] = {"<<=", ">>=", "...", "##", "->", "::", "++", "--", "<<", ">>", "<=", ">=",
                                  "==", "!=", "&&", "||", "+=", "-=", "*=", "/=", "%=", "&=", "|=", "^="};
    while (i < n) {
        char c = s[i];
        size_t j = i + 1;
        if (isSpaceChar(c)) {
            while (j < n && isSpaceChar(s[j])) ++j;
            out.push_back({Tok::Space, s.substr(i, j - i)});
        } else if (c == '/' && i + 1 < n && s[i + 1] == '/') {
            out.push_back({Tok::Comment, s.substr(i)});
            break;
        } else if (c == '/' && i + 1 < n && s[i + 1] == '*') {
            size_t e = s.find("*/", i + 2);
            if (e == std::string::npos) {
                out.push_back({Tok::Comment, s.substr(i)});
                inComment = true;
                break;
            }
            j = e + 2;
            out.push_back({Tok::Comment, s.substr(i, j - i)});
        } else if (std::isalpha(static_cast<unsigned char>(c)) || c == '_') {
            while (j < n && isIdentChar(s[j])) ++j;
            out.push_back({Tok::Ident, s.substr(i, j - i)});
        } else if (std::isdigit(static_cast<unsigned char>(c)) ||
                   (c == '.' && i + 1 < n && std::isdigit(static_cast<unsigned char>(s[i + 1])))) {
            while (j < n) {
                if (isIdentChar(s[j]) || s[j] == '.') ++j;
                else if ((s[j] == '+' || s[j] == '-') && std::strchr("eEpP", s[j - 1])) ++j;
                else break;
            }
            out.push_back({Tok::Number, s.substr(i, j - i)});
        } else if (c == '"' || c == '\'') {
            while (j < n && s[j] != c) j += (s[j] == '\\') ? 2 : 1;
            if (j < n) ++j;
            j = std::min(j, n);
            out.push_back({c == '"' ? Tok::Str : Tok::Chr, s.substr(i, j - i)});
        } else {
            std::string p(1, c);
            for (const char *m : multi) {
                if (s.compare(i, std::strlen(m), m) == 0) {
                    p = m;
                    break;
                }
            }
            j = i + p.size();
            out.push_back({Tok::Punct, p});
        }
        i = j;
    }
    return out;
}

std::string join(const std::vector<Tok> &toks) {
    std::string s;
    for (const auto &t : toks) s += t.text;
    return s;
}

/* comments inside a directive count as one space */
std::vector<Tok> withoutComments(std::vector<Tok> toks) {
    for (auto &t : toks) {
        if (t.kind == Tok::Comment) t = {Tok::Space, " "};
    }
    return toks;
}

void trim(std::vector<Tok> &toks) {
    while (!toks.empty() && toks.back().kind == Tok::Space) toks.pop_back();
    size_t k = 0;
    while (k < toks.size() && toks[k].kind == Tok::Space) ++k;
    toks.erase(toks.begin(), toks.begin() + static_cast<long>(k));
}

/* keeps `-NEG` from becoming `--1` when NEG is `-1`: two characters that
   would fuse into one token get a space between them */
bool wouldFuse(char a, char b) {
    if (isIdentChar(a) && isIdentChar(b)) return true;
    static const char *opChars = "+-*/%&|^<>=!.:#";
    return std::strchr(opChars, a) && std::strchr(opChars, b);
}

/* ---------------- macros & conditionals ---------------- */

struct Macro {
    bool functionLike = false;
    std::vector<std::string> params;
    bool variadic = false;
    std::vector<Tok> body;
    int file = 0, line = 0;
};

struct Cond {
    bool parentActive;
    bool active;   /* this branch is being kept */
    bool taken;    /* some branch of this #if has been kept already */
    bool seenElse;
    int outLine;   /* where the #if is, for "unterminated" */
};

const std::set<std::string> &standardHeaders() {
    static const std::set<std::string> h = {
        "stdio.h", "stdlib.h", "string.h", "stdarg.h", "stdbool.h", "ctype.h", "math.h", "limits.h",
        "stddef.h", "stdint.h", "assert.h", "time.h", "float.h", "errno.h", "iostream", "cstdio", "cstdlib",
        "cstring", "cmath", "string", "vector"};
    return h;
}

class Preprocessor {
  public:
    bool run(const std::string &path, std::string &out) {
        std::string text;
        if (!readFile(path, text)) return false;
        g_sourceFiles = {path};
        g_lineOrigins.clear();
        processFile(0, text);
        out.clear();
        g_sourceLines.clear();
        for (size_t i = 0; i < outLines_.size(); ++i) {
            out += outLines_[i] + outEnds_[i];
            g_sourceLines.push_back(outLines_[i]);
        }
        return true;
    }

  private:
    std::map<std::string, Macro> macros_;
    std::vector<std::string> outLines_, outEnds_;
    std::set<std::string> onceFiles_;
    int includeDepth_ = 0;
    int curFile_ = 0, curLine_ = 0, curOutLine_ = 0, expandDepth_ = 0;
    std::string pendingInclude_;

    static bool readFile(const std::string &path, std::string &text) {
        std::ifstream f(path, std::ios::binary);
        if (!f) return false;
        std::ostringstream ss;
        ss << f.rdbuf();
        text = ss.str();
        return true;
    }

    void error(int col, const std::string &msg) { reportDiagnostic(curOutLine_, col, "", msg, "Preprocessor error"); }
    void warning(int col, const std::string &msg) {
        reportDiagnostic(curOutLine_, col, "", msg, "Preprocessor warning");
    }

    void emit(const std::string &content, const std::string &ending, const std::string &original, bool expanded) {
        outLines_.push_back(content);
        outEnds_.push_back(ending);
        g_lineOrigins.push_back({curFile_, curLine_, original, expanded});
    }

    void processFile(int fileIdx, const std::string &text) {
        /* physical lines, keeping each line's own ending */
        std::vector<std::string> lines, ends;
        for (size_t start = 0; start < text.size();) {
            size_t nl = text.find('\n', start);
            if (nl == std::string::npos) {
                lines.push_back(text.substr(start));
                ends.push_back("");
                break;
            }
            lines.push_back(text.substr(start, nl - start));
            ends.push_back("\n");
            start = nl + 1;
        }
        int savedFile = curFile_;
        std::vector<Cond> conds;
        bool inComment = false;
        for (size_t i = 0; i < lines.size(); ++i) {
            curFile_ = fileIdx;
            curLine_ = static_cast<int>(i) + 1;
            curOutLine_ = static_cast<int>(outLines_.size()) + 1;
            const std::string &content = lines[i];
            bool active = conds.empty() || conds.back().active;
            size_t p = content.find_first_not_of(" \t");
            if (!inComment && p != std::string::npos && content[p] == '#') {
                /* a directive, with its `\`-continued lines */
                std::string logical = content;
                size_t extra = 0;
                auto continues = [](const std::string &s) {
                    size_t e = s.find_last_not_of('\r');
                    return e != std::string::npos && s[e] == '\\';
                };
                while (continues(logical) && i + extra + 1 < lines.size()) {
                    logical.erase(logical.find_last_not_of('\r'));
                    ++extra;
                    logical += lines[i + extra];
                }
                directive(logical, p, conds, active, inComment);
                for (size_t k = 0; k <= extra; ++k) {
                    curLine_ = static_cast<int>(i + k) + 1;
                    emit("", ends[i + k], lines[i + k], false);
                }
                i += extra;
                if (!pendingInclude_.empty()) {
                    std::string inc = pendingInclude_;
                    pendingInclude_.clear();
                    include(inc);
                }
                continue;
            }
            std::vector<Tok> toks = tokenize(content, inComment);
            if (!active) {
                emit("", ends[i], content, false);
                continue;
            }
            bool usesMacro = false;
            for (const auto &t : toks) {
                if (t.kind == Tok::Ident && (macros_.count(t.text) || t.text == "__LINE__" || t.text == "__FILE__")) {
                    usesMacro = true;
                }
            }
            if (!usesMacro) {
                emit(content, ends[i], content, false);
                continue;
            }
            std::string expanded = join(expand(toks, {}));
            emit(expanded, ends[i], content, expanded != content);
        }
        for (const auto &c : conds) {
            reportDiagnostic(c.outLine, 1, "", "unterminated conditional directive (#if without #endif)",
                             "Preprocessor error");
        }
        curFile_ = savedFile;
    }

    /* ---- directives ---- */

    void directive(const std::string &logical, size_t hashPos, std::vector<Cond> &conds, bool active,
                   bool &inComment) {
        std::string rest = logical.substr(hashPos + 1);
        std::vector<Tok> toks = withoutComments(tokenize(rest, inComment));
        int col = static_cast<int>(hashPos) + 1;
        size_t k = 0;
        while (k < toks.size() && toks[k].kind == Tok::Space) ++k;
        if (k >= toks.size()) return; /* `#` alone: the null directive */
        if (toks[k].kind == Tok::Number) return; /* `# 12 "file"` line markers */
        std::string name = toks[k].text;
        std::vector<Tok> args(toks.begin() + static_cast<long>(k) + 1, toks.end());
        trim(args);

        if (name == "if" || name == "ifdef" || name == "ifndef") {
            if (!active) {
                conds.push_back({false, false, true, false, curOutLine_});
                return;
            }
            bool v;
            if (name == "if") {
                v = evaluate(args, col);
            } else {
                if (args.empty() || args[0].kind != Tok::Ident) {
                    error(col, "#" + name + " expects a macro name");
                    v = false;
                } else {
                    v = macros_.count(args[0].text) != 0;
                    if (name == "ifndef") v = !v;
                }
            }
            conds.push_back({true, v, v, false, curOutLine_});
            return;
        }
        if (name == "elif" || name == "else" || name == "endif") {
            if (conds.empty()) {
                error(col, "#" + name + " without #if");
                return;
            }
            Cond &c = conds.back();
            if (name == "endif") {
                conds.pop_back();
                return;
            }
            if (c.seenElse) {
                error(col, "#" + name + " after #else");
                return;
            }
            if (name == "else") {
                c.seenElse = true;
                c.active = c.parentActive && !c.taken;
                c.taken = true;
            } else if (!c.parentActive || c.taken) {
                c.active = false;
            } else {
                c.active = evaluate(args, col);
                c.taken = c.active;
            }
            return;
        }
        if (!active) return; /* anything else in a skipped group is ignored */

        if (name == "define") {
            define(args, col);
        } else if (name == "undef") {
            if (args.empty() || args[0].kind != Tok::Ident) error(col, "#undef expects a macro name");
            else macros_.erase(args[0].text);
        } else if (name == "include") {
            includeDirective(args, col);
        } else if (name == "error") {
            error(col, "#error " + join(args));
        } else if (name == "warning") {
            warning(col, "#warning " + join(args));
        } else if (name == "pragma") {
            if (!args.empty() && args[0].text == "once") onceFiles_.insert(g_sourceFiles[curFile_]);
        } else if (name == "line") {
            /* accepted; positions keep referring to the real file and line */
        } else {
            error(col, "invalid preprocessing directive '#" + name + "'");
        }
    }

    void define(std::vector<Tok> toks, int col) {
        if (toks.empty() || toks[0].kind != Tok::Ident) {
            error(col, "macro name must be an identifier");
            return;
        }
        Macro m;
        m.file = curFile_;
        m.line = curLine_;
        std::string name = toks[0].text;
        if (name == "defined") {
            error(col, "'defined' cannot be used as a macro name");
            return;
        }
        size_t k = 1;
        if (k < toks.size() && toks[k].text == "(") { /* no space before '(': function-like */
            m.functionLike = true;
            ++k;
            bool expectParam = true, closed = false;
            for (; k < toks.size(); ++k) {
                const Tok &t = toks[k];
                if (t.kind == Tok::Space) continue;
                if (t.text == ")") {
                    closed = true;
                    ++k;
                    break;
                }
                if (expectParam && t.text == "...") {
                    m.variadic = true;
                    expectParam = false;
                } else if (expectParam && t.kind == Tok::Ident && !m.variadic) {
                    for (const auto &p : m.params) {
                        if (p == t.text) {
                            error(col, "duplicate macro parameter '" + t.text + "'");
                            return;
                        }
                    }
                    m.params.push_back(t.text);
                    expectParam = false;
                } else if (!expectParam && t.text == ",") {
                    expectParam = true;
                } else {
                    error(col, "invalid parameter list in the definition of macro '" + name + "'");
                    return;
                }
            }
            if (!closed) {
                error(col, "missing ')' in the parameter list of macro '" + name + "'");
                return;
            }
        }
        m.body.assign(toks.begin() + static_cast<long>(k), toks.end());
        trim(m.body);
        /* `#` must stringize a parameter; `##` needs something on both sides */
        for (size_t i = 0; i < m.body.size(); ++i) {
            if (m.body[i].text == "##" && (i == 0 || i + 1 == m.body.size())) {
                error(col, "'##' cannot appear at either end of a macro expansion");
                return;
            }
            if (m.functionLike && m.body[i].text == "#") {
                size_t j = i + 1;
                while (j < m.body.size() && m.body[j].kind == Tok::Space) ++j;
                bool param = j < m.body.size() && (isParam(m, m.body[j].text));
                if (!param) {
                    error(col, "'#' is not followed by a macro parameter");
                    return;
                }
            }
        }
        auto old = macros_.find(name);
        if (old != macros_.end()) {
            const Macro &o = old->second;
            auto normalized = [](const std::vector<Tok> &b) {
                std::string s;
                for (const auto &t : b) s += t.kind == Tok::Space ? " " : t.text;
                return s;
            };
            if (o.functionLike != m.functionLike || o.params != m.params || o.variadic != m.variadic ||
                normalized(o.body) != normalized(m.body)) {
                warning(col, "'" + name + "' macro redefined (previous definition at " +
                                 (o.file == 0 ? std::string() : g_sourceFiles[o.file] + ":") + "line " +
                                 std::to_string(o.line) + ")");
            }
        }
        macros_[name] = m;
    }

    static bool isParam(const Macro &m, const std::string &s) {
        if (m.variadic && s == "__VA_ARGS__") return true;
        for (const auto &p : m.params) {
            if (p == s) return true;
        }
        return false;
    }

    void includeDirective(std::vector<Tok> args, int col) {
        if (!args.empty() && args[0].kind == Tok::Ident) { /* `#include MACRO` */
            args = expand(args, {});
            trim(args);
        }
        std::string file;
        bool system = false;
        if (args.size() == 1 && args[0].kind == Tok::Str && args[0].text.size() >= 2) {
            file = args[0].text.substr(1, args[0].text.size() - 2);
        } else if (!args.empty() && args[0].text == "<") {
            system = true;
            size_t k = 1;
            for (; k < args.size() && args[k].text != ">"; ++k) file += args[k].text;
            if (k >= args.size()) file.clear();
        }
        if (file.empty()) {
            error(col, "#include expects \"FILENAME\" or <FILENAME>");
            return;
        }
        if (system) {
            if (!standardHeaders().count(file)) {
                error(col, "'" + file + "' file not found (only the standard headers are known; their "
                                        "library functions are built into this language)");
            }
            return; /* nothing to include: printf, malloc, ... are keywords here */
        }
        const std::string &current = g_sourceFiles[curFile_];
        size_t slash = current.find_last_of('/');
        std::string path = (slash == std::string::npos ? std::string() : current.substr(0, slash + 1)) + file;
        std::string probe;
        if (!readFile(path, probe)) {
            error(col, "'" + file + "' file not found");
            return;
        }
        if (includeDepth_ >= 200) {
            error(col, "#include nested too deeply (is '" + file + "' including itself?)");
            return;
        }
        pendingInclude_ = path;
    }

    void include(const std::string &path) {
        if (onceFiles_.count(path)) return;
        std::string text;
        readFile(path, text);
        int idx = -1;
        for (size_t i = 0; i < g_sourceFiles.size(); ++i) {
            if (g_sourceFiles[i] == path) idx = static_cast<int>(i);
        }
        if (idx < 0) {
            g_sourceFiles.push_back(path);
            idx = static_cast<int>(g_sourceFiles.size()) - 1;
        }
        int savedLine = curLine_;
        ++includeDepth_;
        processFile(idx, text);
        --includeDepth_;
        curLine_ = savedLine;
    }

    /* ---- macro expansion ---- */

    void append(std::vector<Tok> &out, const std::vector<Tok> &more, bool fromExpansion) {
        if (more.empty()) return;
        if (fromExpansion && !out.empty() && !out.back().text.empty() && !more.front().text.empty() &&
            wouldFuse(out.back().text.back(), more.front().text.front())) {
            out.push_back({Tok::Space, " "});
        }
        out.insert(out.end(), more.begin(), more.end());
    }

    std::vector<Tok> expand(const std::vector<Tok> &in, const std::set<std::string> &disabled) {
        std::vector<Tok> out;
        if (++expandDepth_ > 200) {
            error(1, "macro expansion nested too deeply");
            --expandDepth_;
            return in;
        }
        bool afterExpansion = false;
        for (size_t i = 0; i < in.size(); ++i) {
            const Tok &t = in[i];
            if (t.kind != Tok::Ident) {
                append(out, {t}, afterExpansion);
                afterExpansion = false;
                continue;
            }
            if (t.text == "__LINE__" || t.text == "__FILE__") {
                append(out, {t.text == "__LINE__" ? Tok{Tok::Number, std::to_string(curLine_)}
                                                  : Tok{Tok::Str, "\"" + g_sourceFiles[curFile_] + "\""}},
                       true);
                afterExpansion = true;
                continue;
            }
            auto it = macros_.find(t.text);
            if (it == macros_.end() || disabled.count(t.text)) {
                append(out, {t}, afterExpansion);
                afterExpansion = false;
                continue;
            }
            const Macro &m = it->second;
            std::set<std::string> inner = disabled;
            inner.insert(t.text);
            if (!m.functionLike) {
                append(out, expand(m.body, inner), true);
                afterExpansion = true;
                continue;
            }
            /* function-like: only an invocation when '(' follows */
            size_t j = i + 1;
            while (j < in.size() && (in[j].kind == Tok::Space || in[j].kind == Tok::Comment)) ++j;
            if (j >= in.size() || in[j].text != "(") {
                append(out, {t}, afterExpansion);
                afterExpansion = false;
                continue;
            }
            std::vector<std::vector<Tok>> args(1);
            int depth = 0;
            size_t k = j + 1;
            bool closed = false;
            for (; k < in.size(); ++k) {
                const Tok &a = in[k];
                if (a.text == "(") ++depth;
                if (a.text == ")") {
                    if (depth == 0) {
                        closed = true;
                        break;
                    }
                    --depth;
                }
                if (a.text == "," && depth == 0) {
                    args.emplace_back();
                    continue;
                }
                args.back().push_back(a);
            }
            if (!closed) {
                error(1, "unterminated argument list invoking macro '" + t.text +
                             "' (a macro call's arguments must be on one line)");
                append(out, {t}, afterExpansion);
                afterExpansion = false;
                continue;
            }
            for (auto &a : args) trim(a);
            if (m.params.empty() && args.size() == 1 && args[0].empty()) args.clear();
            size_t want = m.params.size();
            if ((!m.variadic && args.size() != want) || (m.variadic && args.size() < want)) {
                error(1, "macro '" + t.text + "' requires " + std::string(m.variadic ? "at least " : "") +
                             std::to_string(want) + " argument" + (want == 1 ? "" : "s") + ", but " +
                             std::to_string(args.size()) + (args.size() == 1 ? " was" : " were") + " given");
                append(out, std::vector<Tok>(in.begin() + static_cast<long>(i), in.begin() + static_cast<long>(k) + 1),
                       afterExpansion);
                afterExpansion = false;
                i = k;
                continue;
            }
            std::map<std::string, std::vector<Tok>> raw;
            for (size_t p = 0; p < want; ++p) raw[m.params[p]] = args[p];
            if (m.variadic) {
                std::vector<Tok> va;
                for (size_t p = want; p < args.size(); ++p) {
                    if (p > want) va.push_back({Tok::Punct, ","});
                    va.insert(va.end(), args[p].begin(), args[p].end());
                }
                raw["__VA_ARGS__"] = va;
            }
            append(out, expand(substitute(m, raw, disabled), inner), true);
            afterExpansion = true;
            i = k;
        }
        --expandDepth_;
        return out;
    }

    static std::string stringize(const std::vector<Tok> &arg) {
        std::string s = "\"";
        for (const auto &t : arg) {
            if (t.kind == Tok::Space || t.kind == Tok::Comment) {
                if (s.back() != ' ' && s.size() > 1) s += ' ';
                continue;
            }
            if (t.kind == Tok::Str || t.kind == Tok::Chr) {
                for (char c : t.text) {
                    if (c == '"' || c == '\\') s += '\\';
                    s += c;
                }
            } else {
                s += t.text;
            }
        }
        while (s.size() > 1 && s.back() == ' ') s.pop_back();
        return s + "\"";
    }

    std::vector<Tok> substitute(const Macro &m, const std::map<std::string, std::vector<Tok>> &raw,
                                const std::set<std::string> &disabled) {
        auto neighbour = [&](size_t i, int dir) -> std::string { /* nearest non-space body token */
            for (long j = static_cast<long>(i) + dir; j >= 0 && j < static_cast<long>(m.body.size()); j += dir) {
                if (m.body[j].kind != Tok::Space) return m.body[j].text;
            }
            return "";
        };
        std::vector<Tok> r;
        for (size_t i = 0; i < m.body.size(); ++i) {
            const Tok &t = m.body[i];
            if (t.text == "#" && m.functionLike) {
                size_t j = i + 1;
                while (j < m.body.size() && m.body[j].kind == Tok::Space) ++j;
                r.push_back({Tok::Str, stringize(raw.at(m.body[j].text))});
                i = j;
                continue;
            }
            auto a = t.kind == Tok::Ident ? raw.find(t.text) : raw.end();
            if (a == raw.end()) {
                r.push_back(t);
            } else if (neighbour(i, -1) == "##" || neighbour(i, +1) == "##") {
                r.insert(r.end(), a->second.begin(), a->second.end()); /* operands of ## are not expanded */
            } else {
                std::vector<Tok> e = expand(a->second, disabled);
                r.insert(r.end(), e.begin(), e.end());
            }
        }
        /* token pasting */
        std::vector<Tok> pasted;
        for (size_t i = 0; i < r.size(); ++i) {
            if (r[i].text != "##") {
                pasted.push_back(r[i]);
                continue;
            }
            while (!pasted.empty() && pasted.back().kind == Tok::Space) pasted.pop_back();
            size_t j = i + 1;
            while (j < r.size() && r[j].kind == Tok::Space) ++j;
            std::string left = pasted.empty() ? "" : pasted.back().text;
            std::string right = j < r.size() ? r[j].text : "";
            if (!pasted.empty()) pasted.pop_back();
            bool lc = false;
            std::vector<Tok> fused = tokenize(left + right, lc);
            pasted.insert(pasted.end(), fused.begin(), fused.end());
            i = j;
        }
        return pasted;
    }

    /* ---- #if expressions ---- */

    bool evaluate(const std::vector<Tok> &args, int col) {
        /* `defined X` / `defined(X)` first, before macros are expanded */
        std::vector<Tok> t;
        for (size_t i = 0; i < args.size(); ++i) {
            if (args[i].kind == Tok::Ident && args[i].text == "defined") {
                size_t j = i + 1;
                auto skip = [&] { while (j < args.size() && args[j].kind == Tok::Space) ++j; };
                skip();
                bool paren = j < args.size() && args[j].text == "(";
                if (paren) ++j, skip();
                if (j >= args.size() || args[j].kind != Tok::Ident) {
                    error(col, "'defined' must be followed by a macro name");
                    return false;
                }
                bool d = macros_.count(args[j].text) != 0;
                ++j;
                if (paren) {
                    skip();
                    if (j >= args.size() || args[j].text != ")") {
                        error(col, "missing ')' after 'defined'");
                        return false;
                    }
                    ++j;
                }
                t.push_back({Tok::Number, d ? "1" : "0"});
                i = j - 1;
                continue;
            }
            t.push_back(args[i]);
        }
        std::vector<Tok> e = expand(t, {});
        expr_.clear();
        for (const auto &x : e) {
            if (x.kind != Tok::Space && x.kind != Tok::Comment) expr_.push_back(x);
        }
        if (expr_.empty()) {
            error(col, "#if with no expression");
            return false;
        }
        pos_ = 0;
        exprError_.clear();
        long long v = ternary();
        if (exprError_.empty() && pos_ < expr_.size()) exprError_ = "unexpected '" + expr_[pos_].text + "'";
        if (!exprError_.empty()) {
            error(col, "invalid #if expression: " + exprError_);
            return false;
        }
        return v != 0;
    }

    std::vector<Tok> expr_;
    size_t pos_ = 0;
    std::string exprError_;

    bool accept(const char *op) {
        if (pos_ < expr_.size() && expr_[pos_].text == op) {
            ++pos_;
            return true;
        }
        return false;
    }
    void fail(const std::string &why) {
        if (exprError_.empty()) exprError_ = why;
    }

    long long ternary() {
        long long c = binary(0);
        if (accept("?")) {
            long long a = ternary();
            if (!accept(":")) fail("expected ':' in '?:'");
            long long b = ternary();
            return c ? a : b;
        }
        return c;
    }

    /* precedence climbing over C's binary operators */
    long long binary(int level) {
        static const std::vector<std::vector<std::string>> levels = {
            {"||"}, {"&&"}, {"|"}, {"^"}, {"&"}, {"==", "!="}, {"<", ">", "<=", ">="}, {"<<", ">>"}, {"+", "-"},
            {"*", "/", "%"}};
        if (level == static_cast<int>(levels.size())) return unary();
        long long v = binary(level + 1);
        for (;;) {
            std::string op;
            for (const auto &o : levels[level]) {
                if (pos_ < expr_.size() && expr_[pos_].text == o) op = o;
            }
            if (op.empty()) return v;
            ++pos_;
            long long r = binary(level + 1);
            if (op == "||") v = v || r;
            else if (op == "&&") v = v && r;
            else if (op == "|") v |= r;
            else if (op == "^") v ^= r;
            else if (op == "&") v &= r;
            else if (op == "==") v = v == r;
            else if (op == "!=") v = v != r;
            else if (op == "<") v = v < r;
            else if (op == ">") v = v > r;
            else if (op == "<=") v = v <= r;
            else if (op == ">=") v = v >= r;
            else if (op == "<<") v = (r < 0 || r > 62) ? 0 : v << r;
            else if (op == ">>") v = (r < 0 || r > 62) ? 0 : v >> r;
            else if (op == "+") v += r;
            else if (op == "-") v -= r;
            else if (op == "*") v *= r;
            else if (r == 0) {
                fail("division by zero");
                v = 0;
            } else {
                v = op == "/" ? v / r : v % r;
            }
        }
    }

    long long unary() {
        if (accept("!")) return !unary();
        if (accept("~")) return ~unary();
        if (accept("-")) return -unary();
        if (accept("+")) return unary();
        if (accept("(")) {
            long long v = ternary();
            if (!accept(")")) fail("missing ')'");
            return v;
        }
        if (pos_ >= expr_.size()) {
            fail("expression ends too early");
            return 0;
        }
        const Tok &t = expr_[pos_++];
        if (t.kind == Tok::Number) {
            const std::string &s = t.text;
            size_t i = 0;
            int base = 10;
            if (s.size() > 1 && s[0] == '0' && (s[1] == 'x' || s[1] == 'X')) base = 16, i = 2;
            else if (s.size() > 1 && s[0] == '0' && (s[1] == 'b' || s[1] == 'B')) base = 2, i = 2;
            else if (s.size() > 1 && s[0] == '0') base = 8, i = 1;
            long long v = 0;
            for (; i < s.size() && std::isxdigit(static_cast<unsigned char>(s[i])); ++i) {
                int d = std::isdigit(static_cast<unsigned char>(s[i])) ? s[i] - '0' : std::tolower(s[i]) - 'a' + 10;
                if (d >= base) break;
                v = v * base + d;
            }
            if (i < s.size() && !std::strchr("uUlL", s[i])) fail("'" + s + "' is not an integer");
            return v;
        }
        if (t.kind == Tok::Chr) {
            if (t.text.size() >= 3 && t.text[1] == '\\') {
                switch (t.text[2]) {
                    case 'n': return '\n';
                    case 't': return '\t';
                    case '0': return 0;
                    default: return static_cast<unsigned char>(t.text[2]);
                }
            }
            return t.text.size() >= 3 ? static_cast<unsigned char>(t.text[1]) : 0;
        }
        if (t.kind == Tok::Ident) return t.text == "true" ? 1 : 0; /* an unknown name is 0, as in C */
        fail("unexpected '" + t.text + "'");
        return 0;
    }
};

} // namespace

bool preprocessFile(const std::string &path, std::string &out) {
    Preprocessor pp;
    return pp.run(path, out);
}

FILE *openPreprocessed(const std::string &path) {
    std::string text;
    if (!preprocessFile(path, text)) return nullptr;
    FILE *f = std::tmpfile();
    if (!f) return nullptr;
    std::fwrite(text.data(), 1, text.size(), f);
    std::rewind(f);
    return f;
}
