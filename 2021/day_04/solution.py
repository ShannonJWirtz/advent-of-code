import numpy as np

def get_inputs(file_name):
    with open(file_name) as f:
        lines = f.readlines()
    tables = []
    for i, line in enumerate(lines):
        if i == 0:
            numbers = [int(i) for i in line.strip().split(',')]
        elif line == '\n':
            tables.append([])
        else:
            tables[-1].append([int(i) for i in line.strip().split(' ') if i not in ['', ' ']])
    tables = np.array([table for table in tables])
    return numbers, tables

def get_winner_score(numbers, tables):
    marks = np.zeros(tables.shape)

    while np.all(np.sum(marks, 1) < 5) and np.all(np.sum(marks, 2) < 5):
        number = numbers.pop(0)
        marks += (tables == number)

    if np.all(np.sum(marks, 1) == 5):
        table = np.where(np.sum(marks, 1) == 5)[0]
    else:
        table_num = np.where(np.sum(marks, 2) == 5)[0]

    return int(round(np.sum((tables[table_num] * (1-marks[table_num]))) * number))

def get_score(marks, tables, winner_number, number):
    return int(round(np.sum((tables[winner_number] * (1-marks[winner_number]))) * number))

def get_final_winner_score(numbers, tables):
    marks = np.zeros(tables.shape)
    table_numbers = set(range(len(tables)))
    while len(numbers) > 0:
        number = numbers.pop(0)
        marks += (tables == number)
        for i in np.where(np.sum(marks, 1) == 5)[0]:
            if i in table_numbers:
                table_numbers.remove(i)
                score = get_score(marks, tables, i, number)
        for i in np.where(np.sum(marks, 2) == 5)[0]:
            if i in table_numbers:
                table_numbers.remove(i)
                score = get_score(marks, tables, i, number)
    return score

if __name__ == '__main__':
    print('The first answer is: ', get_winner_score(*get_inputs('input.txt')))
    print('The first answer is: ', get_final_winner_score(*get_inputs('input.txt')))
