CC      = g++
CFLAGS  = -std=c++17 -Wall -Wno-unused-function -Wno-class-memaccess -O2 -Iinclude -Ibuild -I../shared/include

BISON   = bison
FLEX    = flex

TARGET  = syntax_analyzer

COMMON      = src/common.cpp src/ast.cpp
SHARED_SRC  = ../shared/src/token_type.cpp
CONVERTER   = src/token_converter.cpp
MAIN        = src/main.cpp

.PHONY: all clean

all: $(TARGET)

build:
	mkdir -p build

build/parser.tab.cpp build/parser.tab.hpp: src/parser.y | build
	$(BISON) -d -o build/parser.tab.cpp src/parser.y

build/lex.yy.cpp: src/scanner.l build/parser.tab.hpp
	$(FLEX) -o build/lex.yy.cpp src/scanner.l

$(TARGET): build/parser.tab.cpp build/lex.yy.cpp $(COMMON) $(SHARED_SRC) $(CONVERTER) $(MAIN)
	$(CC) $(CFLAGS) -o $(TARGET) \
	build/parser.tab.cpp \
	build/lex.yy.cpp \
	$(COMMON) \
	$(SHARED_SRC) \
	$(CONVERTER) \
	$(MAIN)

clean:
	rm -rf build $(TARGET) logs
