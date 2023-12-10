def get_inputs(filename):
    with open(filename) as f: 
        lines = [line.strip() for line in f.readlines()]
    graph = dict()
    h, w = len(lines), len(lines[0])
    for i, line in enumerate(lines):
        for j, symbol in enumerate(line):
            graph[(i,j)] = dict()
            graph[(i,j)]['symbol'] = symbol
            graph[(i,j)]['pipe_destinations'] = get_pipe_destinations(i, j, h, w, symbol)
            graph[(i,j)]['adjacent_nodes'] = []
            for vdir, hdir in [(-1,0), (1,0), (0,-1), (0,1)]:
                if 0 <= i + vdir < h and \
                    0 <= j + hdir < w:
                    graph[(i,j)]['adjacent_nodes'].append((i + vdir, j + hdir))
    return graph

pipe_directions = {
    '|': ((-1, 0), (1,0)),
    '-': ((0, -1), (0,1)),
    'L': ((-1, 0), (0,1)),
    'J': ((-1, 0), (0,-1)),
    '7': ((1, 0), (0,-1)),
    'F': ((1, 0), (0,1)),
}

def get_pipe_destinations(vpos, hpos, h, w, symbol):
    if symbol in '.S':
        return []
    destinations = []
    for vdir, hdir in pipe_directions[symbol]:
        if 0 <= vpos + vdir < h and \
            0 <= hpos + hdir < w:
            destinations.append((vpos + vdir,hpos + hdir))
    return destinations
            
def part1(filename):
    graph = get_inputs(filename)
    start = next(k for k, v in graph.items() if v['symbol'] == 'S')
    for node in graph[start]['adjacent_nodes']:
        if not start in graph[node]['pipe_destinations']:
            continue
        node_list, current_node = [start, node], node
        if not graph[current_node]['pipe_destinations']:
            continue
        next_node = next(n for n in graph[current_node]['pipe_destinations'] if n != start)
        while next_node not in node_list:
            previous_node = current_node
            current_node = next_node
            node_list.append(next_node)
            if not graph[current_node]['pipe_destinations']:
                break
            next_node = next(n for n in graph[current_node]['pipe_destinations'] if n not in [current_node, previous_node])
        if next_node == start:
            break
    return int(len(node_list)/2)

            
def part2(filename):
    graph = get_inputs(filename)
    start = next(k for k, v in graph.items() if v['symbol'] == 'S')

    for node in graph[start]['adjacent_nodes']:
        if not start in graph[node]['pipe_destinations']:
            continue
        node_list = [start, node]
        parity = 0
        if not graph[node_list[-1]]['pipe_destinations']:
            continue
        next_node = next(n for n in graph[node_list[-1]]['pipe_destinations'] if n != start)
        while next_node not in node_list:
            node_list.append(next_node)
            parity += get_parity(graph, *node_list[-3:])
            if not graph[next_node]['pipe_destinations']:
                break
            next_node = next(n for n in graph[node_list[-1]]['pipe_destinations'] if n != node_list[-2])
        if next_node == start:
            node_list.append(start)
            parity += get_parity(graph, *node_list[-3:])
            break

    parity = int(parity / abs(parity))
    inside = get_inside(graph, node_list, parity)
    return len(inside)

"""
Working out parity
L,R
(-1,0): (0,1), (0,-1)
(0,1): (1,0), (-1,0)
(1,0): (0,-1), (0,1)
(0,-1): (-1,0), (1,0)
pd[0] * nd[1] - pd[1] * nd[0]
Left is negative, Right is positive
"""

def get_directions(previous_node, current_node, next_node):
    prev_dir = (previous_node[0] - current_node[0], previous_node[1] - current_node[1])
    next_dir = (next_node[0] - current_node[0], next_node[1] - current_node[1])
    return prev_dir, next_dir

def get_parity(graph, previous_node, current_node, next_node):
    prev_dir, next_dir = get_directions(previous_node, current_node, next_node)
    return prev_dir[0] * next_dir[1] - prev_dir[1] * next_dir[0]


    
def get_inside(graph, node_list, parity):
    inside_boundary = set()
    node_list = node_list[:-1].copy()

    for previous_node, current_node, next_node in \
        zip(node_list[-1:] + node_list[:-1], 
            node_list, 
            node_list[1:] + node_list[:1]):
        prev_dir, next_dir = get_directions(previous_node, current_node, next_node)
        inside_nodes = [(current_node[0] - prev_dir[1] * parity,
                       current_node[1] + prev_dir[0] * parity)]
        if next_node != inside_nodes[-1]:
            inside_nodes.append(
                (current_node[0] - prev_dir[0],
                       current_node[1] - prev_dir[1]))
        for inside_node in inside_nodes:
            if inside_node in graph.keys() and not inside_node in node_list:
                inside_boundary.add(inside_node)
    inside = inside_boundary.copy()
    to_check = set()
    for node in inside:
        for adj_node in graph[node]['adjacent_nodes']:
            if not adj_node in inside | set(node_list):
                to_check.add(node)

    while to_check:
        node = to_check.pop()
        for adj_node in graph[node]['adjacent_nodes']:
            if not adj_node in inside | set(node_list):
                to_check.add(adj_node)
                inside.add(adj_node)

    return inside


if __name__ == '__main__':
    print(f"Part 1: {part1('input.txt')}")
    print(f"Part 2: {part2('input.txt')}")