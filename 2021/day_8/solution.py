def get_inputs(filename):
    with open(filename) as f:
        lines = f.readlines()

    return [[[encoded_number.strip() for encoded_number in section.split(' ')]
         for section in line.split(' | ')]
        for line in lines]

unique_counts = [2, 4, 3, 7]

def get_easy_digit_counts(inputs):

    return sum(
        1
        for line in inputs
        for number in line[1]
        if len(number) in unique_counts
    )

easy_number_segcount_map = {2: 1, 4: 4, 3: 7, 7: 8}

#See bottom of part2_analysis.py for workings out
def get_decoded_output(line):
    unique_codes, output = line[0], line[1]

    number_encodings = { easy_number_segcount_map[len(code)] : code for code in unique_codes if len(code) in easy_number_segcount_map.keys()}

    segment_codes = {seg: [code for code in unique_codes if seg in code] for seg in 'abcdefg'}

    missing_segment_codes = {seg: [code for code in unique_codes if seg not in code] for seg in 'abcdefg'}

    number_encodings[2] = [codes[0] for codes in missing_segment_codes.values() if len(codes) == 1][0]

    five_six = [codes for codes in missing_segment_codes.values() if len(codes) == 2 and number_encodings[1] not in codes][0]

    number_encodings[5] = [code for code in five_six if len(code) == 5][0]

    number_encodings[6] = [code for code in five_six if len(code) == 6][0]

    number_encodings[0] = [ codes[0]
                           for codes in
                           [[code for code in codes if code not in number_encodings.values()]
                            for seg, codes in segment_codes.items()]
                           if len(codes) == 1
                           ][0]

    number_encodings[3] = [code for code in unique_codes if code not in number_encodings.values() and len(code) == 5][0]

    number_encodings[9] = [code for code in unique_codes if code not in number_encodings.values() and len(code) == 6][0]

    number_decodings = {frozenset(code): number for number, code in number_encodings.items()}

    return sum(number_decodings[frozenset(code)] * 10**(i) for i, code in enumerate(reversed(output)))

def get_output_sum(inputs):
    return sum(get_decoded_output(line) for line in inputs)

if __name__ == '__main__':

    print('First answer is: ', get_easy_digit_counts(get_inputs('input.txt')))
    print('Second answer is: ', get_output_sum(get_inputs('input.txt')))
