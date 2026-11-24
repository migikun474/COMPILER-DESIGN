#ifndef OPT_H
#define OPT_H

#include <ostream>
#include <string>
#include <utility>
#include <vector>

#include "tac.h"

namespace tac {

struct OptStats {
    int before = 0, after = 0;
    int inlined = 0;
    int folded = 0;
    int simplified = 0;
    int common = 0;
    int copies = 0;
    int coalesced = 0;
    int dead = 0;
    int jumps = 0;
    int unreachable = 0;
};

OptStats optimize(Program &program);
std::vector<std::pair<int, std::string>> uninitializedReads(Program &program);
void printStats(const OptStats &s, std::ostream &out);

}

#endif
