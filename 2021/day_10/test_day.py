import solution

def test_get_syntax_error():
    inputs = solution.get_inputs('test_input.txt')
    assert(solution.get_syntax_error(inputs[0])) == ''
    assert(solution.get_syntax_error(inputs[1])) == ''
    assert(solution.get_syntax_error(inputs[2])) == '}'


def test_get_syntax_error_score():
    inputs = solution.get_inputs('test_input.txt')
    assert(solution.get_syntax_error_score(inputs) == 26397)

def test_get_incomplete_lines_score():
    inputs = solution.get_inputs('test_input.txt')
    assert(solution.get_incomplete_lines_score(inputs) == 288957)
