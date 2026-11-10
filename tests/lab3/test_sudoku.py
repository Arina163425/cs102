import unittest
from src.lab3.sudoku import read_sudoku, group, get_row, get_col, get_block, find_empty_positions, find_possible_values, solve, check_solution, generate_sudoku
class SudokuTestCase(unittest.TestCase):
    def test_group(self):
        self.assertEqual(group([1,2,3,4,5,6,7,8,9], 3), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertEqual(group([], 4), [])
        self.assertEqual(group([1,2,3,4,5], 1), [[1], [2], [3], [4], [5]])

    def test_get_row(self):
        self.assertEqual(get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0)), ['.', '8', '9'])
        self.assertEqual(get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 2)), ['.', '8', '9'])

    def test_get_col(self):
        self.assertEqual(get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2)), ['3', '6', '9'])
        self.assertEqual(get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 2)), ['3', '6', '9'])

    def test_get_block(self):
        grid = read_sudoku('src/lab3/puzzle1.txt')
        self.assertEqual(get_block(grid, (8, 8)), ['2', '8', '.', '.', '.', '5', '.', '7', '9'])
        self.assertEqual(get_block(grid, (6, 6)), ['2', '8', '.', '.', '.', '5', '.', '7', '9'])

    def test_find_empty_positions(self):
        self.assertEqual(find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']]), (2, 0))
        self.assertEqual(find_empty_positions([['1', '.', '3'], ['4', '5', '6'], ['.', '8', '9']]), (0, 1))
        self.assertIsNone(find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]))

    def test_find_possible_values(self):
        grid = read_sudoku('src/lab3/puzzle1.txt')
        self.assertEqual(find_possible_values(grid, (4,7)), {'2', '5', '9'})
        self.assertEqual(find_possible_values(grid, (0, 2)), {'1', '2', '4'})

    def test_solve(self):
        grid = read_sudoku('src/lab3/puzzle1.txt')
        self.assertEqual(solve(grid), [['5', '3', '4', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'], ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'], ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'], ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'], ['3', '4', '5', '2', '8', '6', '1', '7', '9']])

        grid = read_sudoku('src/lab3/puzzle1.txt')
        grid[0][3] = '1'
        self.assertIsNone(solve(grid))
    def test_check_solution(self):
        grid = read_sudoku('src/lab3/puzzle1.txt')
        solution = solve(grid)
        self.assertIsNotNone(solution)
        self.assertTrue(check_solution(solution))

        solution[0][0] = solution[0][1]
        self.assertFalse(check_solution(solution))

    def test_generate_sudoku(self):
        grid = generate_sudoku(40)

        empty_count = 0
        for row in grid:
            for cell in row:
                if cell == '.':
                    empty_count += 1

        self.assertEqual(empty_count, 41)

        solution = solve(grid)
        self.assertIsNotNone(solution)
        self.assertTrue(check_solution(solution))

        grid = generate_sudoku(81)

        empty_count = 0
        for row in grid:
            for cell in row:
                if cell == '.':
                    empty_count += 1

        self.assertEqual(empty_count, 0)
        self.assertTrue(check_solution(grid))

        grid = generate_sudoku(100)

        empty_count = 0
        for row in grid:
            for cell in row:
                if cell == '.':
                    empty_count += 1

        self.assertEqual(empty_count, 0)
        self.assertTrue(check_solution(grid))
