import solution


def test_get_min_fuel_consumption():
    assert(solution.get_min_fuel_consumption(solution.get_inputs('test_input.txt')) == 37)

def test_get_min_fuel_consumption_pt2():
    assert(solution.get_min_fuel_consumption_pt2(solution.get_inputs('test_input.txt')) == 168)
