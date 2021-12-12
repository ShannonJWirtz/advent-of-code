from string import ascii_lowercase, ascii_uppercase
from collections import defaultdict

def get_inputs(filename):
    with open(filename) as f:
        lines = f.readlines()

    small_caves, all_caves = set(), set()

    next_caves = defaultdict(set)

    for line in lines:
        cave1, cave2 = line.strip().split('-')
        all_caves.add(cave1)
        all_caves.add(cave2)
        if cave1[0] in ascii_lowercase: small_caves.add(cave1)
        if cave2[0] in ascii_lowercase: small_caves.add(cave2)
        next_caves[cave1].add(cave2)
        next_caves[cave2].add(cave1)

    next_caves = dict(next_caves)

    return small_caves, all_caves, next_caves

def calculate_paths(filename):
    small_caves, available_caves, next_caves = get_inputs(filename)

    available_caves.remove('start')
    cave = 'start'
    paths = dict(count=0)

    def pathfinder(cave, paths):
        for next_cave in next_caves[cave].intersection(available_caves):
            if next_cave in small_caves: available_caves.remove(next_cave)
            if next_cave == 'end':
                paths['count'] += 1
            else:
                pathfinder(next_cave, paths)
            available_caves.add(next_cave)

    pathfinder(cave, paths)

    return paths['count']

def calculate_paths_pt2(filename):
    small_caves, available_caves, next_caves = get_inputs(filename)

    small_cave_counts = {cave : 0 for cave in small_caves}

    available_caves.remove('start')
    cave = 'start'
    paths = dict(count=0)

    def pathfinder(cave, paths):
        if len({count for count in small_cave_counts.values() if count > 1}):
            unavailable_small_caves = set([cave for cave, count in small_cave_counts.items() if count > 0])
        else:
            unavailable_small_caves = set()

        for next_cave in next_caves[cave].intersection(available_caves - unavailable_small_caves):
            if next_cave in small_caves: small_cave_counts[next_cave] += 1
            if next_cave == 'end':
                paths['count'] += 1
            else:
                pathfinder(next_cave, paths)
            if next_cave in small_caves: small_cave_counts[next_cave] -= 1

    pathfinder(cave, paths)

    return paths['count']

if __name__ == '__main__':

    print('First answer is: ', calculate_paths('input.txt'))
    print('Second answer is: ', calculate_paths_pt2('input.txt'))
