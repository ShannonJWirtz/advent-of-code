from numpy import Inf
from itertools import chain

def get_inputs(filename, pt2=False):
    with open(filename) as f:
        inputs = [[int(i) for i in line.strip()] for line in f.readlines()]

    if not pt2: return inputs

    inputs = [
        list(chain.from_iterable([[ ((n-1+i) % 9) + 1 for n in line] for i in range(5)]))
        for line in inputs
    ]
    inputs = list(chain.from_iterable([[ [((n-1+j) % 9) + 1 for n in line] for line in inputs ] for j in range(5)]))
    return inputs

def get_initial_graph(filename, pt2=False):
    inputs = get_inputs(filename, pt2)
    length = len(inputs)
    last_index = length - 1
    graph = {(i,j) : dict() for i in range(length) for j in range(length)}

    for i in range(length):
        for j in range(length):
            graph[(i,j)]['d'] = inputs[i][j]
            neighbours = set()
            if i > 0: neighbours.add((i-1,j))
            if i < last_index: neighbours.add((i+1,j))
            if j > 0: neighbours.add((i,j-1))
            if j < last_index: neighbours.add((i,j+1))
            graph[(i,j)]['neighbours'] = neighbours

    return graph, (last_index, last_index)


def reconstruct_path(camefrom, current):
    final_path = [current]
    while (0,0) not in final_path:
        final_path.insert(0, camefrom[current])
        current = camefrom[current]

    return final_path


def get_safest_path_and_score_astar(filename, pt2=False):
    graph, end = get_initial_graph(filename, pt2)
    neighbours = {
        node: info['neighbours']
        for node, info in graph.items()
    }

    h = lambda x: abs(end[0] - x[0]) + abs(end[1] - x[1])

    openset = {(0,0)}

    camefrom = dict()

    gscore = { node: Inf for node in graph.keys() }
    gscore[(0,0)] = 0

    fscore = { node: Inf for node in graph.keys() }
    fscore[(0,0)] = h((0,0))

    while len(openset) > 0:
        current = min(openset, key=lambda x: fscore[x])
        if current == end:
             return reconstruct_path(camefrom, current), gscore[current]

        openset.remove(current)
        for neighbour in neighbours[current]:
            tentative_gscore = gscore[current] + graph[neighbour]['d']
            if tentative_gscore < gscore[neighbour]:
                camefrom[neighbour] = current
                gscore[neighbour] = tentative_gscore
                fscore[neighbour] = tentative_gscore + h(neighbour)
                if neighbour not in openset:
                    openset.add(neighbour)

    return [], Inf

if __name__ == '__main__':
    print('First answer is:', get_safest_path_and_score_astar('input.txt')[1])
    print('Second answer is:', get_safest_path_and_score_astar('input.txt', pt2=True)[1])
