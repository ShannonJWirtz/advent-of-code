import solution as soln

def test_get_bin_from_hex():
    assert(soln.get_bin_from_hex('D2FE28') == '110100101111111000101000')
    assert(soln.get_bin_from_hex('38006F45291200') == '00111000000000000110111101000101001010010001001000000000')
    assert(soln.get_bin_from_hex('EE00D40C823060') == '11101110000000001101010000001100100000100011000001100000')

def test_get_input_bin_string():
    assert(soln.get_input_binstring('test_input1.txt') == '11101110000000001101010000001100100000100011000001100000')

def test_get_next_packet_metadata():
    metadata1 = dict(version=6, type=4)
    test_metadata1 = soln.get_next_packet_metadata('110100101111111000101000')
    assert(metadata1 == test_metadata1)

    metadata2 = dict(version=1, type=6, length_type=0, length=27)
    test_metadata2 = soln.get_next_packet_metadata('00111000000000000110111101000101001010010001001000000000')
    assert(metadata2 == test_metadata2)

    metadata3 = dict(version=1, type=6, length_type=1, length=1)
    test_metadata3 = soln.get_next_packet_metadata('00111010000000000110111101000101001010010001001000000000')
    assert(metadata3 == test_metadata3)


def test_split_literal():
    value, remaining = soln.split_literal('101111111000101000')

    assert(value == 2021)
    assert(remaining == '000')

def test_get_version_sum():
    assert(soln.get_version_sum_from_file('test_input2.txt') == 16)
    assert(soln.get_version_sum_from_file('test_input3.txt') == 12)
    assert(soln.get_version_sum_from_file('test_input4.txt') == 23)
    assert(soln.get_version_sum_from_file('test_input5.txt') == 31)

def test_get_version_sum():
    assert(soln.get_evaluation_from_file('test_input6.txt') == 3)
    assert(soln.get_evaluation_from_file('test_input7.txt') == 54)
    assert(soln.get_evaluation_from_file('test_input8.txt') == 7)
    assert(soln.get_evaluation_from_file('test_input9.txt') == 9)
