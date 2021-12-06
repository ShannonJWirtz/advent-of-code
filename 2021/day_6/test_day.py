import solution

def test_get_lanternfish_number():
    inputs = solution.get_inputs('test_input.txt')
    assert(solution.get_lanternfish_number(inputs) == 5934)
