import solution
import numpy as np

bit_array = np.array([[1,0,1], [1,1,1], [1,0,1]])

def test_get_bit_array():
    with open('test_input.txt') as f:
        assert((solution.get_bit_array(f.readlines()) == bit_array).all())

def test_get_power_consumption():
    assert(solution.get_power_consumption(bit_array) == 10)

def test_get_decimal_from_bit_sequence():
    assert(solution.get_decimal_from_bit_sequence([0,1,0,1]) == 5)

def test_get_rating():
    assert(solution.get_rating(bit_array, 'oxygen generator') == 5)
    assert(solution.get_rating(bit_array, 'CO2 scrubber') == 7)

def test_get_life_support_rating():
    assert(solution.get_life_support_rating(bit_array) == 35)


def test_part_2():
    with open('test_input_2.txt') as f:
        pt2_bit_array = solution.get_bit_array(f.readlines())

    assert(solution.get_rating(pt2_bit_array, 'oxygen generator') == 23)
    assert(solution.get_rating(pt2_bit_array, 'CO2 scrubber') == 10)
    assert(solution.get_life_support_rating(pt2_bit_array) == 230)
