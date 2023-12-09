def get_inputs(filename):
    with open(filename) as f: 
        lines =  [tuple(tuple(int(number) for number in rnge.split('-')) 
                        for rnge in line.split(','))
                  for line in f.readlines()]
    return lines

def part1(filename):
    inputs = get_inputs(filename)
    return sum((one[0] >= two[0] and one[1] <= two[1])
               or (one[0] <= two[0] and one[1] >= two[1])
               for one, two in inputs)

def part2(filename):
    inputs = get_inputs(filename)
    return sum((one[0] <= two[1] and (one[0] >= two[0] or one[1] >= two[0]))
               or (two[0] <= one[1] and (two[0] >= one[0] or two[1] >= one[0]))
               for one, two in inputs)

if __name__ == '__main__':
    print(f"Part 1: {part1('input.txt')}")
    print(f"Part 2: {part2('input.txt')}")