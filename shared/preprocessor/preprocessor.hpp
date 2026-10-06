#ifndef SHARED_PREPROCESSOR_HPP
#define SHARED_PREPROCESSOR_HPP

/* =====================================================================
   PREPROCESSOR -- the stage before lexing
   ---------------------------------------------------------------------
   Supports the directives a C program uses day to day:

     #define NAME body            object-like macro
     #define NAME(a, b) body      function-like macro (also `...` /
                                  __VA_ARGS__, `#param` stringizing and
                                  `x ## y` token pasting)
     #undef NAME
     #if expr / #ifdef / #ifndef / #elif / #else / #endif
                                  (integer expressions, `defined NAME`)
     #include "file"              relative to the including file
     #include <header>            standard headers are accepted and ignored:
                                  printf, malloc, free, ... are keywords
                                  of this language, nothing to declare
     #error / #warning / #pragma (ignored)
     __LINE__, __FILE__

   Line structure is preserved: every input line produces exactly one
   output line (a directive, a skipped #if branch or a `\`-continued line
   becomes an empty line), and a file with no directives and no macro
   uses comes out byte-for-byte unchanged. Text inside comments and
   string/char literals is never expanded.

   The output is also stored line by line in g_sourceLines, with
   g_lineOrigins recording the file and line each one came from, so every
   diagnostic -- lexical, syntax or semantic -- is reported at the place
   the user wrote (see diagnostics.hpp). Problems are reported as
   "Preprocessor error" / "Preprocessor warning". */

#include <cstdio>
#include <string>

/* Preprocesses `path` into `out`. Returns false only when `path` cannot
   be read (nothing is reported then; the driver prints its usual
   "could not open file" message). */
bool preprocessFile(const std::string &path, std::string &out);

/* What every driver does with it: preprocesses `path` and returns a
   stream over the result, ready to hand to a flex scanner as yyin
   (nullptr when `path` cannot be read). */
FILE *openPreprocessed(const std::string &path);

#endif
