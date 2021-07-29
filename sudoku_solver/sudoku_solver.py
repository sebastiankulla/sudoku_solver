from typing import List
from copy import deepcopy

class SudokuNotValidError(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class Sudoku:
    field: List

    def __init__(self, field: List) -> None:
        self.field = field
        self.check_validity()

    def check_validity(self) -> None:
        """ checks if the entered Sudoku is valid"""
        num_rows = len(self.field)
        if num_rows != 9:
            raise SudokuNotValidError(f'Sudoku consists of more or less than 9 rows')

        possible_numbers = [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for idx_row, row in enumerate(self.field):
            if len(row) != 9:
                raise SudokuNotValidError(f'Row {idx_row} consists of more or less than 9 columns')
            for idx_column, column in enumerate(row):
                if self.field[idx_row][idx_column] not in possible_numbers:
                    raise SudokuNotValidError(f'Number in box {[idx_row, idx_column]} is not valid')

    def check_location_is_safe(self, row: int, column: int) -> bool:
        """ checks if the number in box[row, column] causes some errors"""
        return self.row_is_safe(row) and self.column_is_safe(column) and self.box_is_safe(row, column)

    def row_is_safe(self, row: int) -> bool:
        all_row_numbers = self.field[row]
        return not self.contains_duplicated_numbers(all_row_numbers)

    def column_is_safe(self, column: int) -> bool:
        all_column_numbers = list(list(zip(*self.field))[column])
        return not self.contains_duplicated_numbers(all_column_numbers)

    def box_is_safe(self, row: int, column: int) -> bool:
        box_row_indices = [row - (row % 3), row + 1 - (row % 3), row + 2 - (row % 3)]
        box_column_indices = [column - (column % 3), column + 1 - (column % 3), column + 2 - (column % 3)]
        all_square_numbers = [self.field[row_idx][column_idx] for row_idx in box_row_indices for column_idx in
                              box_column_indices]
        return not self.contains_duplicated_numbers(all_square_numbers)


    @staticmethod
    def contains_duplicated_numbers(numbers: List) -> bool:
        """ checks if there are duplicated numbers in a list of integers"""
        for number in range(1, 10):
            if numbers.count(number) > 1:
                return True
        else:
            return False

    def get_next_free_box(self):
        for idx_row in range(9):
            for idx_column in range(9):
                if self.field[idx_row][idx_column] == -1:
                    return idx_row, idx_column
        else:
            return None, None

    def set_box_value(self, row: int, column: int, value: int) -> None:
        self.field[row][column] = value

    def get_box_value(self, row: int, column: int) -> int:
        return self.field[row][column]

    def print_grid(self):
        print('------------------------------')
        for i in range(9):
            print(*self.field[i], sep = '\t')
        print('------------------------------')

    def __eq__(self, other: 'Sudoku') -> bool:
        return self.field == other.field

    def copy(self) -> 'Sudoku':
        return Sudoku(deepcopy(self.field))



def solve_sudoku(sudoku: Sudoku) -> Sudoku:
    def _solve(sudoku: Sudoku) -> bool:
        row_idx, column_idx = sudoku.get_next_free_box()
        if row_idx is None and column_idx is None:
            return True

        for num in range(1, 10):
            sudoku.set_box_value(row_idx, column_idx, num)
            if sudoku.check_location_is_safe(row_idx, column_idx):
                # sudoku.print_grid()
                if _solve(sudoku):
                    return True
        sudoku.set_box_value(row_idx, column_idx, -1)
        return False

    sudoku_temp = sudoku.copy()
    if _solve(sudoku_temp):
        return sudoku_temp
    else:
        raise ValueError

        




if __name__ == '__main__':
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
    new_sudoku.print_grid()
    solution = solve_sudoku(new_sudoku)
    solution.print_grid()
