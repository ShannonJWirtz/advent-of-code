from collections import Counter, defaultdict

def get_inputs(filename):
    with open(filename) as f:
        lines = f.readlines()

    template = lines[0].strip()

    instructions = dict(
        line.strip().split(' -> ')
        for line in lines[2:]
    )

    return template, instructions


def part1(filename, steps = 10):
    template, instructions = get_inputs(filename)

    for step in range(steps):
        i = 0
        while i < len(template) - 1:
            if template[i:i+2] in instructions.keys():
                template = template[:i+1] + instructions[template[i:i+2]] + template[i+1:]
                i += 1
            i += 1

    counter = Counter(template)
    return max(counter.values()) - min(counter.values())


def get_next_paircounts(paircounts, instructions):
    paircount_updates = defaultdict(int)
    for key, value in paircounts.items():
        if key in instructions.keys():
            to_insert = instructions[key]
            paircount_updates[key[0] + to_insert] += value
            paircount_updates[to_insert + key[1]] += value
        else:
            paircount_updates[key] = value

    return paircount_updates


def part2(filename, steps = 10):
    template, instructions = get_inputs(filename)

    template = '~' + template + '*'
    paircounts = Counter(template[i:i+2] for i in range(len(template) - 1))

    for step in range(steps):
        paircounts = get_next_paircounts(paircounts, instructions)

    element_counts = Counter()
    for key, value in paircounts.items():
        for char in key:
            if char not in '~*':
                element_counts[char] += value
    
    return int((max(element_counts.values()) - min(element_counts.values()))/2)


if __name__ == '__main__':
    print('First answer is:', part1('input.txt'))
    print('Second answer is:', part2('input.txt', 40))
