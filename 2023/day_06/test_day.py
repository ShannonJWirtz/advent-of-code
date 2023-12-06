import solution

test_times = [7, 15, 30]
test_records = [9, 40, 200]

def test_part1():
    assert(solution.part1(test_times, test_records) == 288)

def test_part2():
    assert(solution.part2(71530, 940200) == 71503)