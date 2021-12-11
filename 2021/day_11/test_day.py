import solution

def test_get_flashes():
    assert(solution.get_flashes(solution.get_inputs('test_input2.txt'), 1) == 9)
    assert(solution.get_flashes(solution.get_inputs('test_input2.txt'), 2) == 9)

    assert(solution.get_flashes(solution.get_inputs('test_input3.txt'), 1) == 0)
    assert(solution.get_flashes(solution.get_inputs('test_input3.txt'), 2) == 4)

    assert(solution.get_flashes(solution.get_inputs('test_input.txt'), 2) == 35)
    assert(solution.get_flashes(solution.get_inputs('test_input.txt'), 100) == 1656)

def test_get_first_total_flashes():
    assert(solution.get_first_total_flashes(solution.get_inputs('test_input.txt')) == 195)
