from string import ascii_letters

def get_inputs(filename):
    with open(filename) as f: return [line.strip() for line in f.readlines()]

def part1(filename):
    inputs = get_inputs(filename)
    offending_items = [set(line[:int(len(line)/2)]) & set(line[int(len(line)/2):]) for line in inputs]
    return sum(ascii_letters.index(item) + 1 for pack in offending_items for item in pack)

def part2(filename):
    inputs = get_inputs(filename)
    priority_total = 0
    for group_packs in zip(inputs[::3], inputs[1::3], inputs[2::3]):
        pack_intersection = set.intersection(*(set(pack) for pack in group_packs))
        priority_total += ascii_letters.index(pack_intersection.pop()) + 1
    return priority_total



if __name__ == '__main__':
    print(f"Part 1: {part1('input.txt')}")
    print(f"Part 2: {part2('input.txt')}")