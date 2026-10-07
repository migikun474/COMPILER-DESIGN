CC      = g++
PARSER  = ../phase2-parser
SEM     = ../phase2b-semantic
SHARED  = ../shared
CFLAGS  = -std=c++17 -Wall -Wno-unused-function -Wno-class-memaccess -O2 \
          -Iinclude -Ibuild -I$(SEM)/include -I$(PARSER)/include -I$(SHARED)

BISON   = bison
FLEX    = flex

TARGET  = tac_generator

# phases 2 and 2b are reused as they are: the grammar and scanner are
# regenerated here from the same sources, and the semantic analyzer's
# sources are compiled in, so neither phase's build directory is touched
PARSER_SRC = $(PARSER)/src/declarators.cpp $(PARSER)/src/scanner_support.cpp $(PARSER)/src/token_converter.cpp
SEM_SRC    = $(SEM)/src/declarations.cpp $(SEM)/src/statements.cpp $(SEM)/src/expressions.cpp \
             $(SEM)/src/cxx.cpp $(SEM)/src/sequencing.cpp $(SEM)/src/report.cpp
IR_SRC     = src/tac.cpp src/gen_expr.cpp src/gen_stmt.cpp src/interp.cpp src/opt.cpp
MAIN       = src/main.cpp
HEADERS    = $(wildcard include/*.h) $(wildcard $(SEM)/include/*.h) $(wildcard $(PARSER)/include/*)
LIBSHARED  = $(SHARED)/build/libshared.a

.PHONY: all clean test $(LIBSHARED)

all: $(TARGET)

$(LIBSHARED):
	$(MAKE) -C $(SHARED)

build:
	mkdir -p build

build/parser.tab.cpp build/parser.tab.hpp: $(PARSER)/src/parser.y | build
	$(BISON) -d -o build/parser.tab.cpp $(PARSER)/src/parser.y

build/lex.yy.cpp: $(PARSER)/src/scanner.l build/parser.tab.hpp
	$(FLEX) -o build/lex.yy.cpp $(PARSER)/src/scanner.l

$(TARGET): build/parser.tab.cpp build/lex.yy.cpp $(PARSER_SRC) $(SEM_SRC) $(IR_SRC) $(MAIN) $(HEADERS) $(LIBSHARED)
	$(CC) $(CFLAGS) -o $(TARGET) build/parser.tab.cpp build/lex.yy.cpp $(PARSER_SRC) $(SEM_SRC) $(IR_SRC) $(MAIN) $(LIBSHARED)

test: $(TARGET)
	./run_tests.sh

clean:
	rm -rf build $(TARGET)
