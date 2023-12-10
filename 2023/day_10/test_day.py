import solution

def test_part1():
    assert(solution.part1('test_data.txt') == 4)
    assert(solution.part1('test_data2.txt') == 4)
    assert(solution.part1('test_data3.txt') == 8)
    assert(solution.part1('test_data4.txt') == 8)

def test_part2():
    assert(solution.part2('test_data.txt') == 1)
    assert(solution.part2('test_data5.txt') == 4)
    assert(solution.part2('test_data6.txt') == 8)
    assert(solution.part2('test_data7.txt') == 10)