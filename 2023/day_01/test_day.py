import solution

test_data = [
    '1abc2',
'pqr3stu8vwx',
'a1b2c3d4e5f',
'treb7uchet'
]

test_data_2 = [
    'two1nine',
'eightwothree',
'abcone2threexyz',
'xtwone3four',
'4nineeightseven2',
'zoneight234',
'7pqrstsixteen',
]

def test_get_sum():
    assert(solution.get_sum(test_data) == 142)

def test_get_calibration_value_part_2():
    assert(solution.get_calibration_value_part_2(test_data_2[0]) == 29)
    assert(solution.get_calibration_value_part_2(test_data_2[1]) == 83)
    assert(solution.get_calibration_value_part_2(test_data_2[2]) == 13)
    assert(solution.get_calibration_value_part_2(test_data_2[3]) == 24)
    assert(solution.get_calibration_value_part_2(test_data_2[4]) == 42)
    assert(solution.get_calibration_value_part_2(test_data_2[5]) == 14)
    assert(solution.get_calibration_value_part_2(test_data_2[6]) == 76)

def test_get_sum_part_2():
    assert(solution.get_sum_part_2(test_data) == 142)
    assert(solution.get_sum_part_2(test_data_2) == 281)
