import numpy as np

def get_bit_array(lines):
    return np.array([[int(bit) for bit in line.strip()] for line in lines])

def get_decimal_from_bit_sequence(bit_sequence):
    return int(sum(bit * 2**i for i, bit in enumerate(bit_sequence[::-1])))

def get_power_consumption(bit_array):
    bit_averages = np.average(bit_array, 0)
    gamma = get_decimal_from_bit_sequence([round(bit) for bit in bit_averages[::-1]])
    eps = get_decimal_from_bit_sequence([round(1-bit) for bit in bit_averages[::-1]])
    return int(gamma * eps)

def get_rating(bit_array, criteria):

    i = 0
    while  i < len(bit_array[0]) and len(bit_array) > 1:
        section = bit_array[:, i]
        freq = np.average(section)
        if criteria == 'CO2 scrubber' and 0 < freq < 1 :
            value = 0 if freq >= 0.5 else 1
        else:
            value = 1 if freq >= 0.5 else 0
        bit_array = bit_array[section == value]
        i += 1

    return get_decimal_from_bit_sequence(bit_array[0])

def get_life_support_rating(bit_array):
    oxygen = get_rating(bit_array, 'oxygen generator')
    co2 = get_rating(bit_array, 'CO2 scrubber')
    return oxygen * co2

if __name__ == '__main__':

    with open('input.txt') as f:
        bit_array = get_bit_array(f.readlines())

    print('problem 1 answer: ', get_power_consumption(bit_array))
    print('problem 2 answer: ', get_life_support_rating(bit_array))
