def get_instructions_from_raw(lines):
     return [(dir, int(n)) for dir, n in [line.split(' ') for line in lines]]

def final_position_multipled(instructions):
    pos = [0, 0]
    for instr in instructions:
        if instr[0] == 'forward': pos[0] += instr[1]
        elif instr[0] == 'up': pos[1] -= instr[1]
        else: pos[1] += instr[1]
    return pos[0] * pos[1]

def final_position_multipled_pt2(instructions):
    pos = [0, 0]
    aim = 0
    for instr in instructions:
        if instr[0] == 'forward':
            pos[0] += instr[1]
            pos[1] += instr[1] * aim
        elif instr[0] == 'up': aim -= instr[1]
        else: aim += instr[1]
    return pos[0] * pos[1]



if __name__ == '__main__':

    with open('input.txt') as f:
        instructions = get_instructions_from_raw(f.readlines())

    print('problem 1 answer: ', final_position_multipled(instructions))
    print('problem 2 answer: ', final_position_multipled_pt2(instructions))
