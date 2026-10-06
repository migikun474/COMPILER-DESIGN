# The shared library every phase links: one module per section of the
# compiler, built once into build/libshared.a. Phases include headers as
# "module/header.hpp" with -I../shared.
CXX      = g++
CXXFLAGS = -std=c++17 -Wall -O2 -I.
AR       = ar

MODULES  = token diagnostics preprocessor ast types symbol_table
SRC      = token/token_type.cpp token/token_log.cpp diagnostics/diagnostics.cpp preprocessor/preprocessor.cpp \
           ast/ast.cpp types/types.cpp symbol_table/symbol_table.cpp
HEADERS  = $(wildcard $(addsuffix /*.hpp,$(MODULES)))
OBJ      = $(SRC:%.cpp=build/%.o)
LIB      = build/libshared.a

.PHONY: all clean

all: $(LIB)

$(LIB): $(OBJ)
	$(AR) rcs $@ $^

build/%.o: %.cpp $(HEADERS)
	@mkdir -p $(dir $@)
	$(CXX) $(CXXFLAGS) -c $< -o $@

clean:
	rm -rf build
