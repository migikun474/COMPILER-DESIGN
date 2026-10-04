# Phase 4 — MIPS Code Generation

> **Status: not started.** This folder contains only this README. No
> part of the repository emits MIPS assembly, and there is no phase 3
> (TAC) for it to consume yet.

## Planned work (not implemented)

1. Translate TAC (from [`../phase3-ir`](../phase3-ir/README.md)) to MIPS
   assembly with a simple frame layout: every temporary in the stack
   frame, no register allocation.
2. Run-time support for the language's built-ins (`printf`, `scanf`,
   `malloc`/`free`, file I/O). How depends on the target, which is not
   decided yet:
   - **SPIM / MARS simulator** — built-ins implemented as a small MIPS
     run-time library over the simulator's system calls;
   - **MIPS Linux** (cross-assembler + an emulator) — built-ins call the
     C library through the o32 calling convention.
3. Register allocation (linear scan) and peephole optimization.

## What already fixes the target model

The front end already assumes MIPS32 (ILP32): `int`, `long` and
pointers are 4 bytes, `long long` and `double` 8; record layouts and
`sizeof` use these sizes (`../shared/types/types.cpp`, `sizeOf()`,
`layoutRecord()`), and `va_list` is 4 bytes. Function link names are
Itanium-mangled (`_Z3addii`) and can be used directly as labels.

No MIPS assembler or simulator is installed in the development
environment yet.
