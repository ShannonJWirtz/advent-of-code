def get_inputs(filename):
    with open(filename) as f: 
        return [line.strip() for line in f.readlines()]

def main(filename, expansion_factor=2):
    inputs = get_inputs(filename)
    all_dot_rows = [i for i, line in enumerate(inputs) 
                    if all(char == '.' for char in line)]
    all_dot_cols = [j for j in range(len(inputs[0])) 
                    if all(inputs[i][j] == '.' for i in range(len(inputs)))]
    galaxies = []
    for i, line in enumerate(inputs):
        for j, char in enumerate(line):
            if char == '#':
                galaxies.append((i + sum(expansion_factor - 1 
                                         for n in all_dot_rows if n < i),
                                 j + sum(expansion_factor - 1 
                                         for m in all_dot_cols if m < j)))
    lengths_total = 0
    for i, galaxy1 in enumerate(galaxies[:-1]):
        for galaxy2 in galaxies[i+1:]:
            lengths_total += (abs(galaxy1[0] - galaxy2[0]) + 
                              abs(galaxy1[1] - galaxy2[1]))
    
    return lengths_total

def part1(filename): return main(filename)

def part2(filename, expansion_factor): return main(filename, expansion_factor)

if __name__ == '__main__':
    print(f"Part 1: {part1('input.txt')}")
    print(f"Part 2: {part2('input.txt', 1_000_000)}")