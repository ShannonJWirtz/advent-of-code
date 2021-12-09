import solution

def test_get_risk_score_sum():
    assert(solution.get_risk_score_sum(solution.get_inputs('test_input.txt')) == 15)

def test_get_lowest_points():
    assert(solution.get_lowest_points(solution.get_inputs('test_input.txt')) == [(0,1), (0,9), (2,2), (4,6)])

def test_get_basin_size():
    assert(solution.get_basin_size(solution.get_inputs('test_input.txt'), (0,1)) == 3)
    assert(solution.get_basin_size(solution.get_inputs('test_input.txt'), (0,9)) == 9)
    assert(solution.get_basin_size(solution.get_inputs('test_input.txt'), (2,2)) == 14)
    assert(solution.get_basin_size(solution.get_inputs('test_input.txt'), (4,6)) == 9)

def test_get_top_3_basin_size_multiples():
    assert(solution.get_top_3_basin_size_multiples(solution.get_inputs('test_input.txt')) == 1134)
