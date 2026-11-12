# Blind Valley Puzzle Solver

A Python puzzle solver that uses recursive backtracking and constraint checking to fill domino-shaped grid layouts with high, base, and neutral tiles.

## Overview

Blind Valley is a constraint-based grid puzzle. The input defines a board of horizontal and vertical domino slots, together with row and column restrictions. The solver assigns values to each slot while respecting the puzzle rules.

## Puzzle Rules

- Every domino slot must contain either a **High–Base (H–B)**, **Base–High (B–H)**, or **Neutral–Neutral (N–N)** pair.
- Orthogonally adjacent High cells cannot touch other High cells; the same applies to Base cells. Diagonal neighbors are not restricted.
- Row and column constraints specify required counts of High and Base cells. A constraint of `-1` means that count is unrestricted.
- If no valid arrangement is found, the program prints `No solution!`.

## How It Works

The solver processes domino slots from top-left to bottom-right. It attempts **H–B**, then **B–H**, and finally **N–N** for each slot. Recursive backtracking explores candidates and reverses placements when necessary. Constraint and neighbor checks help prune invalid placements.

## Requirements

- Python 3 (standard library only; no third-party dependencies)

## Usage

Run from the repository root:

```bash
python blind_valley.py examples/input1.txt
```

The program prints the solved grid to the terminal. To save that output to a file, use shell redirection:

```bash
python blind_valley.py examples/input1.txt > result.txt
```

## Input Format

The input file contains four constraint lines followed by the domino layout:

1. Required High counts for each row
2. Required Base counts for each row
3. Required High counts for each column
4. Required Base counts for each column
5. Layout rows using `L` / `R` for horizontal slots and `U` / `D` for vertical slots

## Output Format

The output grid uses `H` for High, `B` for Base, and `N` for Neutral. If the puzzle cannot be solved, the output is `No solution!`.

## Examples and Verification

Five sample input/output pairs are included in [`examples/`](examples/). The original source was executed against all five inputs and the output matched each expected result after ignoring trailing whitespace. Sample 3 demonstrates the no-solution case.

```text
examples/
├── input1.txt ... input5.txt
└── output1.txt ... output5.txt
```

## Notes

The source code is retained in its original form. Testing covers the five included sample cases; compatibility with arbitrary malformed inputs is not guaranteed.
