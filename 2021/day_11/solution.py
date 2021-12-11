def get_inputs(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]

def get_adjacents_and_initial_values(inputs):

    h, w = len(inputs), len(inputs[0])

    adjacents = dict()
    initial_values = dict()

    for i, line in enumerate(inputs):
        for j, val in enumerate(line):
            initial_values[(i,j)] = int(val)
            adjacents[(i, j)] = set((n, m)
                                    for n in range(i - 1, i + 2)
                                    for m in range(j - 1, j + 2)
                                    if 0 <= n < h and 0 <= m < w and
                                    not (n, m) == (i, j))

    return adjacents, initial_values

def get_flashes(inputs, num):

    adjacents, values = get_adjacents_and_initial_values(inputs)
    flashes = 0

    for _ in range(num):
        values = {loc: val + 1 for loc, val in values.items()}
        flashed_locs = [loc for loc, val in values.items() if val > 9]

        while len(flashed_locs) > 0:
            flashed_loc = flashed_locs.pop()
            for adj in adjacents[flashed_loc]:
                if values[adj] <= 9:
                    values[adj] += 1
                    if values[adj] > 9:
                        flashed_locs.append(adj)

        flashes += len([val for val in values.values() if val > 9])
        values = {loc: val if val <= 9 else 0 for loc, val in values.items()}

    return flashes

def get_first_total_flashes(inputs):

    adjacents, values = get_adjacents_and_initial_values(inputs)
    total_cells = len(values.values())
    step, last_step_cell_flashes = 0, 0

    while last_step_cell_flashes < total_cells:
        values = {loc: val + 1 for loc, val in values.items()}
        flashed_locs = [loc for loc, val in values.items() if val > 9]

        while len(flashed_locs) > 0:
            flashed_loc = flashed_locs.pop()
            for adj in adjacents[flashed_loc]:
                if values[adj] <= 9:
                    values[adj] += 1
                    if values[adj] > 9:
                        flashed_locs.append(adj)

        step += 1
        last_step_cell_flashes = len([val for val in values.values() if val > 9])
        values = {loc: val if val <= 9 else 0 for loc, val in values.items()}

    return step

if __name__ == '__main__':

    print('First answer is: ', get_flashes(get_inputs('input.txt'), 100))
    print('Second answer is: ', get_first_total_flashes(get_inputs('input.txt')))
