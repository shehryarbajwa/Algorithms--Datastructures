import unittest

def grid_game(steps, n):
    maximum_row_upper_bound = 10**10
    maximum_column_upper_bound = 10**10

    for step in steps:
        split_step = list(map(int, step.split(' ')))
        row_upper_bound = split_step[0]
        column_upper_bound = split_step[1]

        if row_upper_bound < maximum_row_upper_bound:
            maximum_row_upper_bound = row_upper_bound
        if column_upper_bound < maximum_column_upper_bound:
            maximum_column_upper_bound = column_upper_bound
    
    return maximum_column_upper_bound * maximum_row_upper_bound

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(grid_game(['2 1', '3 6', '4 2'], 2), 2)

    def test_case_2(self):
        self.assertEqual(grid_game(['9 1', '0 9', '4 5'], 2), 0)

    


if __name__ == '__main__':
    unittest.main()