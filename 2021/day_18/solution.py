from copy import deepcopy
from math import floor, ceil
from functools import reduce
from itertools import permutations

def snail_number_from_string(string):
    return eval(string.strip())


def get_snail_number_list(filename):
    with open(filename) as f:
        return [snail_number_from_string(line) for line in f.readlines()]


def get_num_locations(number):
    loc, list_of_loc_nums = [], []
    def get_num_locations_inner(number, loc = loc, list_of_loc_nums = list_of_loc_nums):
        if len(loc) < 4:
            for i, num in enumerate(number):
                if type(num) == int: list_of_loc_nums.append((loc + [i], num))
                else: get_num_locations_inner(num, loc + [i], list_of_loc_nums)
        else:
            list_of_loc_nums.append((loc, number))
        return list_of_loc_nums

    return get_num_locations_inner(number)


def get_locs_to_explode(number):
    num_locations = get_num_locations(number)
    return [(i, num_loc) for i, num_loc in enumerate(num_locations)
             if len(num_loc[0]) >= 4 and
             type(num_loc[1]) == list]


def get_locs_to_split(number):
    num_locations = get_num_locations(number)
    return [(i, num_loc) for i, num_loc in enumerate(num_locations)
             if type(num_loc[1]) == int
             and num_loc[1] >= 10]


def return_nested_element(nested_list, loc):
    if len(loc) == 1: return nested_list[loc[0]]
    else: return return_nested_element(nested_list[loc[0]], loc[1:])


def assign_to_nested_element(nested_list, loc, val, add_mode=False, from_dir='NA'):
    if len(loc) == 1:
        if not add_mode:
            nested_list[loc[0]] = val
        else:
            if type(nested_list[loc[0]]) != list:
                nested_list[loc[0]] += val
            else:
                if from_dir == 'right':
                    nested_list[loc[0]][1] += val
                elif from_dir == 'left':
                    nested_list[loc[0]][0] += val
                else:
                    assert(False)

    else: assign_to_nested_element(nested_list[loc[0]], loc[1:], val, add_mode, from_dir)


def reduce_snail_number(number):

    while len(get_locs_to_explode(number)) > 0 or len(get_locs_to_split(number)) > 0:
        while len(get_locs_to_explode(number)) > 0:
            loc = get_locs_to_explode(number)[0]
            number_locations = get_num_locations(number)
            if loc[0] > 0:
                assign_to_nested_element(number, number_locations[loc[0] - 1][0], loc[1][1][0], True, from_dir='right')
            if loc[0] < len(number_locations) - 1:
                assign_to_nested_element(number, number_locations[loc[0] + 1][0], loc[1][1][1], True, from_dir='left')
            assign_to_nested_element(number, loc[1][0], 0, False)

        while len(get_locs_to_split(number)) > 0 and len(get_locs_to_explode(number)) == 0:
            loc = get_locs_to_split(number)[0]
            assign_to_nested_element(number, loc[1][0], [int(floor(loc[1][1]/2)),int(ceil(loc[1][1]/2))])

    return number


def reduce_snail_number_list(list_of_numbers):
    return reduce(lambda x, y: reduce_snail_number([x, y]), list_of_numbers)


def get_magnitude(snail_number):
    if type(snail_number[0]) == int:
        left = snail_number[0] * 3
    else:
        left = get_magnitude(snail_number[0]) * 3
    if type(snail_number[1]) == int:
        right = snail_number[1] * 2
    else:
        right = get_magnitude(snail_number[1]) * 2

    return left + right


def part1(filename):
    return get_magnitude(reduce_snail_number_list(get_snail_number_list('input.txt')))


def part2(filename):
    sn_list = get_snail_number_list(filename)
    pairs = permutations(sn_list, 2)
    magnitudes = [
        get_magnitude(reduce_snail_number_list(deepcopy(pair)))
        for pair in pairs
    ]
    return max(magnitudes)

if __name__ == '__main__':
    print('First answer is:', part1('input.txt'))
    print('First answer is:', part2('input.txt'))
