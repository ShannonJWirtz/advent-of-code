def get_inputs(filename):
    with open(filename) as f: 
        return [[int(i) for i in line.split()] for line in f.readlines()]

def part1(filename):
    inputs = get_inputs(filename)
    total = 0
    for sequence in inputs:
        differences = [sequence]
        while not len(set(differences[-1])) == 1:
            current_seq = differences[-1]
            differences.append([current_seq[i+1] - current_seq[i] 
                               for i in range(len(current_seq)-1)])
        total += sum(difference[-1] for difference in differences)
    return total

def part2(filename):
    inputs = get_inputs(filename)
    total = 0
    for sequence in inputs:
        differences = [sequence]
        while not len(set(differences[-1])) == 1:
            current_seq = differences[-1]
            differences.append([current_seq[i+1] - current_seq[i] 
                               for i in range(len(current_seq)-1)])
        to_subtract = 0
        for first_difference in (difference[0] for difference in differences[1:][::-1]):
            to_subtract = first_difference - to_subtract    
        total += differences[0][0] - to_subtract
    return total


if __name__ == '__main__':
    print(f"Part 1: {part1('input.txt')}")
    print(f"Part 2: {part2('input.txt')}")