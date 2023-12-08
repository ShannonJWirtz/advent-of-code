from math import lcm 

def get_inputs(filename):
    with open(filename) as f: 
        inputs = [line.strip() for line in f.readlines()]
    instructions = inputs[0]
    graph = {}
    for line in inputs[2:]:
        key, destinations = line.split(' = ')
        graph[key] = (
            destinations[1:4],
            destinations[6:9],
        )
    return instructions, graph

def part1(filename):
    instructions, graph = get_inputs(filename)
    step = 0
    node = 'AAA'
    while node != 'ZZZ':
        node = graph[node][instructions[step % len(instructions)]  == 'R']
        step += 1
    return step

def part2(filename):
    instructions, graph = get_inputs(filename)
    nodes = [node for node in graph.keys() if node[-1] == 'A']
    steps = []
    for node in nodes:
        step = 0
        current_node = node
        while current_node[-1] != 'Z':
            current_node = graph[current_node][instructions[step % len(instructions)]  == 'R']
            step += 1
        steps.append(step)
    return lcm(*steps)
                
if __name__ == '__main__':
    print(f"Part 1: {part1('input.txt')}")
    print(f"Part 2: {part2('input.txt')}")