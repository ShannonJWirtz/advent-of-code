import solution

def test_get_easy_digit_counts():
    assert(solution.get_easy_digit_counts(solution.get_inputs('test_input.txt')) == 26)

def test_get_output_sum():
    assert(solution.get_output_sum(solution.get_inputs('test_input.txt')) == 61229)
