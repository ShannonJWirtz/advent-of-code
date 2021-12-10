import solution

def test_get_overlap_number():
    inputs = solution.get_inputs('test_input.txt')
    assert(solution.get_overlap_number(inputs) == 5)

def test_get_overlap_number_pt2():
    inputs = solution.get_inputs('test_input.txt')
    assert(solution.get_overlap_number_pt2(inputs) == 12)
