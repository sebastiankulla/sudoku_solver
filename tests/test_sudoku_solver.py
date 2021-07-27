from sudokusolver import Sudoku, solve_sudoku, SudokuNotValidError
from unittest import TestCase


class SudokuTestsNoError(TestCase):
    def setUp(self) -> None:
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
        self.sudoku = Sudoku(field)

    def test_duplicates_in_row(self):
        self.assertTrue(self.sudoku.row_is_safe(4))

    def test_duplicates_in_column(self):
        self.assertTrue(self.sudoku.column_is_safe(4))

    def test_duplicates_in_box(self):
        self.assertTrue(self.sudoku.box_is_safe(4, 4))



class SudokuTestsError(TestCase):
    def setUp(self) -> None:
        field = [
            [-1, 3, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, 1, 9, 5, -1, -1, -1],
            [-1, -1, 8, -1, -1, -1, -1, 6, -1],
            [8, -1, -1, -1, 6, -1, -1, -1, -1],
            [4, -1, -1, 6, 6, -1, -1, -1, 1],
            [-1, -1, -1, -1, 2, -1, -1, -1, -1],
            [-1, 6, -1, -1, -1, -1, 2, 8, -1],
            [-1, -1, -1, 4, 1, 9, -1, -1, 5],
            [-1, -1, -1, -1, -1, -1, -1, 7, -1]
        ]
        self.sudoku = Sudoku(field)

    def test_duplicates_in_row(self):
        self.assertFalse(self.sudoku.row_is_safe(4))

    def test_duplicates_in_column(self):
        self.assertFalse(self.sudoku.column_is_safe(4))

    def test_duplicates_in_box(self):
        self.assertFalse(self.sudoku.box_is_safe(4, 4))


class SudokuTestsValidity(TestCase):
    def test_field_valid(self) -> None:
        field = [
            [-1, 3, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, 1, 9, 5, -1, -1, -1],
            [-1, -1, 8, -1, -1, -1, -1, 6, -1],
            [8, -1, -1, -1, 6, -1, -1, -1, -1],
            [4, -1, -1, 6, 6, -1, -1, -1, 1],
            [-1, -1, -1, -1, 2, -1, -1, -1, -1],
            [-1, 6, -1, -1, -1, -1, 2, 8, -1],
            [-1, -1, -1, 4, 1, 9, -1, -1, 5],
            [-1, -1, -1, -1, -1, -1, -1, 7, -1]
        ]

        self.assertIsInstance(Sudoku(field), Sudoku)

    def test_field_not_valid_more_columns(self) -> None:
        field = [
            [-1, 3, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, 1, 9, 5, -1, -1, -1],
            [-1, -1, 8, -1, -1, -1, -1, 6, -1],
            [8, -1, -1, -1, 6, -1, -1, -1, -1],
            [4, -1, -1, 6, 6, -1, -1, -1, 1],
            [-1, -1, -1, -1, 2, -1, -1, -1, -1],
            [-1, 6, -1, -1, -1, -1, 2, 8, -1],
            [-1, -1, -1, 4, 1, 9, -1, -1, 5],
            [-1, -1, -1, -1, -1, -1, -1, 7, -1, 1]
        ]
        self.assertRaises(SudokuNotValidError, lambda: Sudoku(field))

    def test_field_not_valid_more_rows(self) -> None:
        field = [
            [-1, 3, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, 1, 9, 5, -1, -1, -1],
            [-1, -1, 8, -1, -1, -1, -1, 6, -1],
            [8, -1, -1, -1, 6, -1, -1, -1, -1],
            [4, -1, -1, 6, 6, -1, -1, -1, 1],
            [-1, -1, -1, -1, 2, -1, -1, -1, -1],
            [-1, 6, -1, -1, -1, -1, 2, 8, -1],
            [-1, -1, -1, 4, 1, 9, -1, -1, 5],
            [-1, -1, -1, -1, -1, -1, -1, 7, -1],
            [-1, -1, -1, -1, -1, -1, -1, 7, -1]
        ]
        self.assertRaises(SudokuNotValidError, lambda: Sudoku(field))

    def test_field_not_valid_wrong_numbers(self) -> None:
        field = [
            [-1, 3, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, 1, 9, 5, -1, -1, -1],
            [-1, -1, 8, -1, -1, -1, -1, 6, -1],
            [8, -1, -1, -1, 6, -1, -1, -1, -1],
            [4, -1, -1, 6, 6, -1, -1, -1, 1],
            [-1, -1, -1, -1, 2, -1, -1, -1, -1],
            [-1, 6, -1, -1, -1, -1, 2, 8, -1],
            [-1, -1, -1, 4, 1, 9, -1, -1, 5],
            [-1, -1, -1, -1, -1, -1, -1, 10, -1]
        ]
        self.assertRaises(SudokuNotValidError, lambda: Sudoku(field))


class SudokuTestsGeneral(TestCase):
    def setUp(self) -> None:
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
        self.sudoku = Sudoku(field)

    def test_get_field(self) -> None:
        self.assertTrue(self.sudoku.get_box_value(0, 1) == 3)

    def test_set_field(self) -> None:
        self.sudoku.set_box_value(0, 1, 9)
        self.assertTrue(self.sudoku.get_box_value(0, 1) == 9)


class SudokuTestsSolver(TestCase):
    def setUp(self) -> None:
        field_empty = [
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

        self.sudoku_empty = Sudoku(field_empty)

        field_solved = [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]
        ]
        self.sudoku_solved_correctly = Sudoku(field_solved)

    def test_solve_sudoku(self):
        solution = solve_sudoku(self.sudoku_empty)
        self.assertTrue(solution == self.sudoku_solved_correctly)