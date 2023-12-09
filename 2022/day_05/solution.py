from string import ascii_uppercase

def get_inputs(filename):
    with open(filename) as f: 
        lines =  f.readlines()
    stack_lines, instruction_lines = lines[:lines.index('\n')], lines[lines.index('\n')+1:]
    stacks = {number: [] for number in stack_lines[-1] if number not in (' ', '\n')}
    for stack in stacks.keys():
        stack_index = stack_lines[-1].index(stack)
        for line in stack_lines[-2::-1]:
            if line[stack_index] not in (' ', '\n'):
                stacks[stack].append(line[stack_index])
    instructions = [tuple(i for i in line if i in stacks.keys()) for line in instruction_lines]
    return stacks, instructions

def part1(filename):
    stacks, instructions = get_inputs(filename)
    words = []
    for move in instructions:
        # stacks[move[2]] += stacks[move[1]][-int(move[0]):][::-1]
        # stacks[move[1]] = stacks[move[1]][:-int(move[0])]
        for _ in range(int(move[0])):
            crate = stacks[move[1]].pop()
            stacks[move[2]].append(crate)
            print( stacks)
        # words.append(''.join(stack[-1] for number, stack in  sorted(stacks.items()) if stack))
    # print(words)
    assert(False)
    return ''.join(stack[-1] for number, stack in  sorted(stacks.items()) if stack)

# s, i = get_inputs('input.txt')
# print(s)

if __name__ == '__main__':
    print(f"Part 1: {part1('input.txt')}")
    # print(f"Part 2: {part2('input.txt')}")