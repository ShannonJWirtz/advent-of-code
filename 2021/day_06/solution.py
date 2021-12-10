from copy import deepcopy

def get_inputs(filename):
    with open(filename) as f:
        lines = f.readlines()

    return [int(i) for i in lines[0].strip().split(',')]

statemap = {i: (i-1) for i in range(1, 9)}
statemap[0] = 6

def get_lanternfish_number(inputs, days):
    empty_state_counts = {key : 0 for key in statemap.keys()}
    state_counts = deepcopy(empty_state_counts)

    for i in inputs:
        state_counts[i] += 1

    for _ in range(days):
        new_state_counts = deepcopy(empty_state_counts)
        for key, value in state_counts.items():
            new_state_counts[statemap[key]] += value
            if key == 0:
                new_state_counts[8] += value
        state_counts = new_state_counts

    return sum(state_counts.values())


if __name__ == '__main__':
    print('First problem answer is: ', get_lanternfish_number(get_inputs('input.txt'), 80))
    print('Second problem answer is: ', get_lanternfish_number(get_inputs('input.txt'), 256))
