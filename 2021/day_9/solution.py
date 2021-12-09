def get_inputs(filename):
    with open(filename) as f:
        lines = f.readlines()

    return [[int(i) for i in line.strip()] for line in lines]

def get_risk_score_sum(inputs):

    h, w = len(inputs), len(inputs[0])

    risk_score_sum = 0

    for i in range(h):
        for j in range(w):
            if (i == 0 or inputs[i-1][j] > inputs[i][j]) and\
            (i == h - 1 or inputs[i+1][j] > inputs[i][j]) and\
            (j == 0 or inputs[i][j-1] > inputs[i][j]) and\
            (j == w - 1 or inputs[i][j+1] > inputs[i][j]):
                risk_score_sum += (1 + inputs[i][j])

    return risk_score_sum

def get_lowest_points(inputs):

    h, w = len(inputs), len(inputs[0])

    lowest_points = []

    for i in range(h):
        for j in range(w):
            if (i == 0 or inputs[i-1][j] > inputs[i][j]) and\
            (i == h - 1 or inputs[i+1][j] > inputs[i][j]) and\
            (j == 0 or inputs[i][j-1] > inputs[i][j]) and\
            (j == w - 1 or inputs[i][j+1] > inputs[i][j]):
                lowest_points.append((i, j))

    return lowest_points

def get_lower_adjacents(inputs, position):
    i, j = position[0], position[1]

    lower_adjacents = []
    if i > 0 and inputs[i - 1][j] > inputs[i][j] and inputs[i - 1][j] < 9:
        lower_adjacents.append((i - 1, j))
    if i < len(inputs) - 1 and inputs[i + 1][j] > inputs[i][j] and inputs[i + 1][j] < 9:
        lower_adjacents.append((i + 1, j))
    if j > 0 and inputs[i][j - 1] > inputs[i][j] and inputs[i][j - 1] < 9:
        lower_adjacents.append((i, j - 1))
    if j < len(inputs[0]) - 1 and inputs[i][j + 1] > inputs[i][j] and inputs[i][j + 1] < 9:
        lower_adjacents.append((i, j + 1))

    return lower_adjacents

def get_basin_size(inputs, loc):

    marked = [loc]
    visited = []

    while len(marked) > 0:
        position = marked.pop()
        marked += [adj for adj in get_lower_adjacents(inputs, position) if adj not in visited and adj not in marked]
        visited.append(position)

    return len(visited)

def get_top_3_basin_size_multiples(inputs):

    lowest_points = get_lowest_points(inputs)
    basin_sizes = [get_basin_size(inputs, loc) for loc in lowest_points]
    basin_sizes.sort()

    return basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]

if __name__ == '__main__':

    print('First answer is: ', get_risk_score_sum(get_inputs('input.txt')))
    print('Second answer is: ', get_top_3_basin_size_multiples(get_inputs('input.txt')))
