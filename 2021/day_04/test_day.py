import solution
import numpy as np

def test_get_inputs():
    with open('test_inputs.txt') as f:
        lines = f.readlines()
    tables = []
    for i, line in enumerate(lines):
        if i == 0:
            numbers = [int(i) for i in line.strip().split(',')]
            first_line = line
        elif line == '\n':
            tables.append([])
        else:
            tables[-1].append([int(i) for i in line.strip().split(' ') if i not in ['', ' ']])
    tables = np.array([table for table in tables])

    numbers_to_test, tables_to_test = solution.get_inputs('test_inputs.txt')
    assert(np.all(numbers_to_test == numbers) and np.all(tables_to_test == tables))

def test_get_winner_score():
    assert(solution.get_winner_score(*solution.get_inputs('test_inputs.txt')) == 4512)

def test_get_final_winner_score():
    assert(solution.get_final_winner_score(*solution.get_inputs('test_inputs.txt')) == 1924)
