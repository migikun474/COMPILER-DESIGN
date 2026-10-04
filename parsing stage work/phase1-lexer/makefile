CC      = g++
SHARED  = ../shared
CFLAGS  = -std=c++17 -Wall -O2 -Iinclude -I$(SHARED)

LEX     = flex

SRC     = src/lexer.l
GEN     = lex.yy.c

TARGET  = lexer

LOGGER       = src/logger.cpp
TOKEN        = src/token.cpp
LIBSHARED    = $(SHARED)/build/libshared.a

.PHONY: all clean $(LIBSHARED)

all: $(TARGET)

$(LIBSHARED):
	$(MAKE) -C $(SHARED)

$(TARGET): $(GEN) $(LOGGER) $(TOKEN) $(wildcard include/*.h) $(LIBSHARED)
	$(CC) $(CFLAGS) \
	-o $(TARGET) \
	$(GEN) \
	$(LOGGER) \
	$(TOKEN) \
	$(LIBSHARED)

$(GEN): $(SRC)
	$(LEX) -o $(GEN) $(SRC)

clean:
	rm -f $(GEN) $(TARGET)
