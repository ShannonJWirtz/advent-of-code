import solution

def test_inputs():
    all_caves = set(['start', 'A', 'b', 'c', 'd', 'end'])
    small_caves = set(['start', 'end', 'b', 'c', 'd'])
    next_caves = dict(
        start = set(['A', 'b']),
        A = set(['start', 'b', 'end', 'c']),
        b = set(['start', 'd', 'end', 'A']),
        c = set(['A']),
        d = set(['b']),
        end = set(['A', 'b'])
        )
    test_small_caves, test_all_caves, test_next_caves = solution.get_inputs('test_input.txt')
    assert(all_caves == test_all_caves)
    assert(small_caves == test_small_caves)
    assert(next_caves == test_next_caves)

def test_calculate_paths():
    assert(solution.calculate_paths('test_input.txt') == 10)
    assert(solution.calculate_paths('test_input2.txt') == 19)
    assert(solution.calculate_paths('test_input3.txt') == 226)

# def test_calculate_paths_list_pt2():
#     with open('test_paths_input.txt') as f:
#         paths_list = set([line.strip() for line in f.readlines()])
#     test_paths_list = set(solution.calculate_paths_list_pt2('test_input.txt'))
#     assert(paths_list == test_paths_list)

def test_calculate_paths_pt2():
    assert(solution.calculate_paths_pt2('test_input.txt') == 36)
    assert(solution.calculate_paths_pt2('test_input2.txt') == 103)
    assert(solution.calculate_paths_pt2('test_input3.txt') == 3509)
