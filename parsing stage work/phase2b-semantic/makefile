CC      = g++
PARSER  = ../phase2-parser
SHARED  = ../shared
CFLAGS  = -std=c++17 -Wall -Wno-unused-function -Wno-class-memaccess -O2 \
          -Iinclude -Ibuild -I$(PARSER)/include -I$(SHARED)

BISON   = bison
FLEX    = flex

TARGET  = semantic_analyzer

# phase 2 is reused as-is: its grammar/scanner are regenerated here from
# the same sources, so phase 2's own build directory is never touched
PARSER_SRC = $(PARSER)/src/declarators.cpp $(PARSER)/src/scanner_support.cpp $(PARSER)/src/token_converter.cpp
SEM_SRC    = src/declarations.cpp src/statements.cpp src/expressions.cpp src/cxx.cpp src/sequencing.cpp src/report.cpp
MAIN       = src/main.cpp
HEADERS    = $(wildcard include/*.h) $(wildcard $(PARSER)/include/*)
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

$(TARGET): build/parser.tab.cpp build/lex.yy.cpp $(PARSER_SRC) $(SEM_SRC) $(MAIN) $(HEADERS) $(LIBSHARED)
	$(CC) $(CFLAGS) -o $(TARGET) build/parser.tab.cpp build/lex.yy.cpp $(PARSER_SRC) $(SEM_SRC) $(MAIN) $(LIBSHARED)

test: $(TARGET)
	./run_tests.sh

clean:
	rm -rf build $(TARGET) logs
