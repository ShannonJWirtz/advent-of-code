def get_inputs(filename):
    with open(filename) as f: return [line.strip() for line in f.readlines()]

def part1(filename):
    inputs = [input.split() for input in get_inputs(filename)]
    games = [('ABC'.index(elf_hand), 'XYZ'.index(your_hand)) for elf_hand, your_hand in inputs]
    score = 0
    for game in games:
        score += game[1] + 1
        if game[1] == game[0]:
            score += 3
        elif game[1] == (game[0] + 1) % 3:
            score += 6
    return score

def part2(filename):
    inputs = [input.split() for input in get_inputs(filename)]
    games = [('ABC'.index(elf_hand), 'XYZ'.index(your_hand)) for elf_hand, your_hand in inputs]
    score = 0
    for game in games:
        score += game[1] * 3
        score += (game[0] + game[1] - 1) % 3 + 1
    return score

if __name__ == '__main__':
    print(f"Part 1: {part1('input.txt')}")
    print(f"Part 2: {part2('input.txt')}")