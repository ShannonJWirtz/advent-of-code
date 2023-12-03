import re

number_words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
number_words_regex = '|'.join(number_words)

def get_calibration_value(line):
    digits = re.findall(r'\d', line)
    return int(digits[0]+ digits[len(digits)-1])

def get_sum(input):
    return sum(
        get_calibration_value(line)
        for line in input
    )

def get_integer_from_string(s):
    if s in number_words:
        return str(number_words.index(s)+1)
    else:
        return s
    

def get_calibration_value_part_2(line):
    first_index, first_number = len(line), ''
    for i in list('123456789') + number_words:
        if i in line and line.index(i) < first_index:
            first_index = line.index(i)
            first_number = i

    last_index, last_number = len(line), ''
    for i in list('123456789') + number_words:
        if i in line and line[::-1].index(i[::-1]) < last_index:
            last_index = line[::-1].index(i[::-1])
            last_number = i

    return int(get_integer_from_string(first_number)+ get_integer_from_string(last_number))

def get_sum_part_2(input):
    return sum(
        get_calibration_value_part_2(line)
        for line in input
    )

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    print('Solution 1 is {}'.format(get_sum(lines)))
    print('Solution 2 is {}'.format(get_sum_part_2(lines)))
