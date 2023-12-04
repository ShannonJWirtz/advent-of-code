import solution

with open('test_data.txt') as f: test_data = [line.strip() for line in f.readlines()]

def test_get_sum_part_1():
    assert(solution.get_sum_part_1(test_data) == 13)

def test_get_sum_part_2():
    assert(solution.get_sum_part_2(test_data) == 30)
