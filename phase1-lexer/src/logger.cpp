#include "logger.h"

#include <cstdio>
#include <filesystem>

namespace fs = std::filesystem;

void writeLexerLog(
    const std::string &sourceFile,
    const std::vector<Diagnostic> &diagnostics)
{
    fs::create_directories("logs");

    std::string filename = fs::path(sourceFile).stem().string();
    std::string logfile = "logs/" + filename + ".log";

    FILE *log = fopen(logfile.c_str(), "w");

    if (!log)
        return;

    fprintf(log,
            "=========================================\n");
    fprintf(log,
            "        LEXICAL ERROR REPORT\n");
    fprintf(log,
            "=========================================\n\n");

    fprintf(log,
            "Source File : %s\n\n",
            sourceFile.c_str());

    if (diagnostics.empty())
    {
        fprintf(log,
                "No lexical errors found.\n");
    }
    else
    {
        int count = 1;

        for (const auto &d : diagnostics)
        {
            fprintf(log,
                    "[%d]\n",
                    count++);

            fprintf(log,
                    "Line    : %d\n",
                    d.line);

            fprintf(log,
                    "Lexeme  : %s\n",
                    d.lexeme.c_str());

            fprintf(log,
                    "Message : %s\n\n",
                    d.message.c_str());
        }

        fprintf(log,
                "-----------------------------------------\n");

        fprintf(log,
                "Total Errors : %zu\n",
                diagnostics.size());
    }

    fclose(log);

    if (!diagnostics.empty())
    {
        printf("Lexical errors found.\n");
        printf("Report written to %s\n",
               logfile.c_str());
    }
}