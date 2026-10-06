CC      = g++
SHARED  = ../shared
CFLAGS  = -std=c++17 -Wall -Wno-unused-function -Wno-class-memaccess -O2 -Iinclude -Ibuild -I$(SHARED)

BISON   = bison
FLEX    = flex

TARGET  = syntax_analyzer

PHASE_SRC   = src/declarators.cpp src/scanner_support.cpp src/token_converter.cpp
MAIN        = src/main.cpp
LIBSHARED   = $(SHARED)/build/libshared.a

.PHONY: all clean $(LIBSHARED)

all: $(TARGET)

$(LIBSHARED):
	$(MAKE) -C $(SHARED)

build:
	mkdir -p build

build/parser.tab.cpp build/parser.tab.hpp: src/parser.y | build
	$(BISON) -d -o build/parser.tab.cpp src/parser.y

build/lex.yy.cpp: src/scanner.l build/parser.tab.hpp
	$(FLEX) -o build/lex.yy.cpp src/scanner.l

$(TARGET): build/parser.tab.cpp build/lex.yy.cpp $(PHASE_SRC) $(MAIN) $(wildcard include/*) $(LIBSHARED)
	$(CC) $(CFLAGS) -o $(TARGET) \
	build/parser.tab.cpp \
	build/lex.yy.cpp \
	$(PHASE_SRC) \
	$(MAIN) \
	$(LIBSHARED)

clean:
	rm -rf build $(TARGET) logs
