import solution

def test_part1():
    assert(solution.part1('test_data.txt') == 374)

def test_part2():
    assert(solution.part2('test_data.txt', 10) == 1030)
    assert(solution.part2('test_data.txt', 100) == 8410)