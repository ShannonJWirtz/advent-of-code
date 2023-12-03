import solution

with open('test_data.txt') as f: test_data = [line.strip() for line in f.readlines()]

def test_get_part_1_sum():
    assert(solution.get_part_1_sum(test_data) == 4361)

def test_get_part_2_sum():
    assert(solution.get_part_2_sum(test_data) == 467835)

