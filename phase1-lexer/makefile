CC      = g++
CFLAGS  = -std=c++17 -Wall -O2
LEX     = flex
SRC     = src/lexer.l
GEN     = lex.yy.c
TARGET  = lexer

.PHONY: all clean

all: $(TARGET)

$(TARGET): $(GEN)
	$(CC) $(CFLAGS) -o $(TARGET) $(GEN)

$(GEN): $(SRC)
	$(LEX) -o $(GEN) $(SRC)

clean:
	rm -f $(GEN) $(TARGET)
