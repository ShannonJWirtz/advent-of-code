import re

NON_SYMBOLS = '0123456789.'

def get_adjacent_positions(lines, line_number, span):
    return [
        (i,j) 
        for i in range(line_number-1, line_number+2)
        for j in range(span[0]-1, span[1]+1)
        if 0 <= i <= len(lines)-1 and 0 <= j <= len(lines[0])-1
    ]

def is_match_relevant(line_number, match, lines):
    return any(lines[pos[0]][pos[1]] not in NON_SYMBOLS 
               for pos in get_adjacent_positions(lines, line_number, match.span()))

def get_part_1_sum(lines):
    total = 0
    for line_number, line in enumerate(lines):
        for match in re.finditer(r'\d+', line):
            if is_match_relevant(line_number, match, lines):
                total += int(match.group(0))
    return total

def is_adjacent(number_ln, number_match, gear_ln, gear_match):
    if not abs(number_ln - gear_ln) <= 1:
        return False
    if number_match.start() - 1 <= gear_match.start() <= number_match.end():
        return True

def get_gear_ratio(line_number, gear, numbers):
    matched_numbers = [
        int(number.group(0))
        for number_ln, line in enumerate(numbers) 
        for number in line
        if is_adjacent(number_ln, number, line_number, gear)
    ]
    if len(matched_numbers) == 2:
        return matched_numbers[0] * matched_numbers[1]
    else:
        return 0
 
def get_part_2_sum(lines):
    numbers = [list(re.finditer(r'\d+', line)) for line in lines]
    total = 0
    for line_number, line in enumerate(lines):
        for gear in re.finditer(r'\*', line):
            total += get_gear_ratio(line_number, gear, numbers)
    return total

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = tuple(line.strip() for line in f.readlines())
    print('Solution 1 is {}'.format(get_part_1_sum(lines)))
    print('Solution 2 is {}'.format(get_part_2_sum(lines)))