CC      = g++
PARSER  = ../phase2-parser
SEM     = ../phase2b-semantic
IR      = ../phase3-ir
SHARED  = ../shared
CFLAGS  = -std=c++17 -Wall -Wno-unused-function -Wno-class-memaccess -O2 \
          -Iinclude -Ibuild -I$(IR)/include -I$(SEM)/include -I$(PARSER)/include -I$(SHARED)

BISON   = bison
FLEX    = flex

TARGET  = mips_generator

# the earlier phases are reused as they are: their sources are compiled in
PARSER_SRC = $(PARSER)/src/declarators.cpp $(PARSER)/src/scanner_support.cpp $(PARSER)/src/token_converter.cpp
SEM_SRC    = $(SEM)/src/declarations.cpp $(SEM)/src/statements.cpp $(SEM)/src/expressions.cpp \
             $(SEM)/src/cxx.cpp $(SEM)/src/sequencing.cpp $(SEM)/src/report.cpp
IR_SRC     = $(IR)/src/tac.cpp $(IR)/src/gen_expr.cpp $(IR)/src/gen_stmt.cpp $(IR)/src/interp.cpp $(IR)/src/opt.cpp
MIPS_SRC   = src/mips.cpp src/main.cpp
HEADERS    = $(wildcard include/*.h) $(wildcard $(IR)/include/*.h) $(wildcard $(SEM)/include/*.h) $(wildcard $(PARSER)/include/*)
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

$(TARGET): build/parser.tab.cpp build/lex.yy.cpp $(PARSER_SRC) $(SEM_SRC) $(IR_SRC) $(MIPS_SRC) $(HEADERS) $(LIBSHARED)
	$(CC) $(CFLAGS) -o $(TARGET) build/parser.tab.cpp build/lex.yy.cpp $(PARSER_SRC) $(SEM_SRC) $(IR_SRC) $(MIPS_SRC) $(LIBSHARED)

test: $(TARGET)
	./run_tests.sh

clean:
	rm -rf build $(TARGET)
