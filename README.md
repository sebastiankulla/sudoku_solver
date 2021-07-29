# Sudokusolver

A small tool that allows solving Soduko via backtracking algorithm.

## Usage

```python
from sudoku_solver import Sudoku, solve_sudoku

field = [
    [-1, 3, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, 1, 9, 5, -1, -1, -1],
    [-1, -1, 8, -1, -1, -1, -1, 6, -1],
    [8, -1, -1, -1, 6, -1, -1, -1, -1],
    [4, -1, -1, 8, -1, -1, -1, -1, 1],
    [-1, -1, -1, -1, 2, -1, -1, -1, -1],
    [-1, 6, -1, -1, -1, -1, 2, 8, -1],
    [-1, -1, -1, 4, 1, 9, -1, -1, 5],
    [-1, -1, -1, -1, -1, -1, -1, 7, -1]
]

new_sudoku = Sudoku(field)
solution = solve_sudoku(new_sudoku)
solution.print_grid()
```
