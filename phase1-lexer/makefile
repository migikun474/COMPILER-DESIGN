CC      = g++
CFLAGS  = -std=c++17 -Wall -O2 -Iinclude

LEX     = flex

SRC     = src/lexer.l
GEN     = lex.yy.c

TARGET  = lexer

LOGGER       = src/logger.cpp
TOKEN        = src/token.cpp
DIAGNOSTICS  = src/diagnostics.cpp

.PHONY: all clean

all: $(TARGET)

$(TARGET): $(GEN) $(LOGGER) $(TOKEN) $(DIAGNOSTICS)
	$(CC) $(CFLAGS) \
	-o $(TARGET) \
	$(GEN) \
	$(LOGGER) \
	$(TOKEN) \
	$(DIAGNOSTICS)

$(GEN): $(SRC)
	$(LEX) -o $(GEN) $(SRC)

clean:
	rm -f $(GEN) $(TARGET)