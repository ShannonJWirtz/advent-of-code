import re

def get_matching_numbers_count(line):
    numbers = [set([int(number) for number in re.findall(r'\d+', group)]) for group in line[line.index(':')+2:].split(' | ')]
    return len(numbers[0] & numbers[1])

def get_card_score_part_1(line):
    matching_numbers_count = get_matching_numbers_count(line)
    if matching_numbers_count == 0:
        return 0
    else:
        return 2**(matching_numbers_count-1)
        
def get_sum_part_1(lines):
    return sum(get_card_score_part_1(line) for line in lines)

def get_sum_part_2(lines):
    totals = [get_matching_numbers_count(line) for line in lines][::-1]
    for i, total in enumerate(totals):
        totals[i] += sum(totals[(i - total):i])
    return sum(totals) + len(lines)

if __name__ == '__main__':
    with open('input.txt') as f: data = [line.strip() for line in f.readlines()]
    print("Solution part 1 is: {}".format(get_sum_part_1(data)))
    print("Solution part 2 is: {}".format(get_sum_part_2(data)))