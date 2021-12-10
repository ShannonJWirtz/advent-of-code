##### PART 2 ANALYSIS #####
# Digit representation
# a
# b c
# d
# e f
# g
numbers_codes = {
    0: set(['a', 'b', 'c', 'e', 'f', 'g']),
    1: set(['c', 'f']),
    2: set(['a', 'c', 'd', 'e', 'g']),
    3: set(['a', 'c', 'd', 'f', 'g']),
    4: set(['b', 'c', 'd', 'f']),
    5: set(['a', 'b', 'd', 'f', 'g']),
    6: set(['a', 'b', 'd', 'e', 'f', 'g']),
    7: set(['a', 'c', 'f']),
    8: set(['a', 'b', 'c', 'd', 'e', 'f', 'g']),
    9: set(['a', 'b', 'c', 'd', 'f', 'g'])
}

segment_numbers = {seg: {number for number, code in numbers_codes.items() if len(code.intersection(set(seg))) > 0} for seg in set('abcdefg')}
non_segment_numbers = {seg: set(range(10)) - numbers for seg, numbers in segment_numbers.items()}
non_segment_numbers

non_segment_numbers

segment_numbers

[(key, value  - set([1, 2, 4, 5, 6, 7, 8])) for key, value in segment_numbers.items()]
[(key, value  - set([1, 4, 7, 8])) for key, value in non_segment_numbers.items()]

[(key, value  - set([0, 1, 2, 4, 7, 8])) for key, value in non_segment_numbers.items()]

#[1:2, 2:5, 3:5, 4:4, 5:5, 6:6, 7:3, 8:7, 9:6, 0:6]
#[6,0] sixes
#[4, 5, 6, 8, 9, 0] top left
# a
# b c
# d
# e f
# g
# Bottom right is missing from exactly number 2, no other segments miss exactly one number, so 2 is figured out [1, 2, 4, 7, 8]
# Top right missing from 5 and 6, which have different segment counts. Top is also missing from exactly two numbers, both of those known [1, 4], so both 5 and 6, top right are figured out [1, 2, 4, 5, 6, 7, 8]
# Of the remaining numbers [0, 3, 9], bottom left is present in exactly . No other segment is present in exactly one number, so zero is figured out  [1, 2, 4, 5, 6, 7, 8]
# The remaining numbers [3, 9] have different counts, so are figured out [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

##### END OF ANALYSIS #####
