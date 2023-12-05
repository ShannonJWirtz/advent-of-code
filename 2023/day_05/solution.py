def get_inputs(input_file):
    with open(input_file) as f: lines = f.readlines()
    seeds = [int(seed) for seed in lines[0][7:].split()]
    maps = []
    for line in lines[2:]:
        if '-' in line:
            maps.append([])
        elif not line.isspace():
            maps[-1].append(tuple(int(number) for number in line.split()))
    return seeds, maps            
        
def part1(input_file):
    seeds, maps = get_inputs(input_file)
    seed_locations = []
    for seed in seeds:
        seed_locations.append(seed)
        for map in maps:
            for row in map:
                if  row[1] <= seed_locations[-1] < row[1] + row[2]:
                    seed_locations[-1] = row[0] + seed_locations[-1] - row[1]
                    break
    return min(seed_locations)

def part2(input_file):
    seeds, maps = get_inputs(input_file)
    seeds_location_ranges = []
    for seed_start, length in zip(seeds[::2], seeds[1::2]):
        seeds_location_ranges.append([(seed_start, seed_start + length - 1)])
        for map in maps:
            map.sort(key = lambda x: x[1])
            source_ranges = seeds_location_ranges[-1].copy()
            destination_ranges = []
            for source_range in source_ranges:
                to_be_mapped = source_range
                for i, row in enumerate(map):
                    if to_be_mapped[0] < row[1]:
                        if to_be_mapped[1] < row[1]:
                            destination_ranges.append(to_be_mapped)
                            break
                        destination_ranges.append((to_be_mapped[0], row[1] - 1))
                        to_be_mapped = (row[1], to_be_mapped[1])
                    if to_be_mapped[0] < row[1] + row[2]:
                        if to_be_mapped[1] < row[1] + row[2]:
                            destination_ranges.append((to_be_mapped[0] - row[1] + row[0], to_be_mapped[1] - row[1] + row[0]))
                            break
                        else:
                            destination_ranges.append((to_be_mapped[0] - row[1] + row[0], row[0] + row[2] - 1))
                            to_be_mapped = (row[1] + row[2], to_be_mapped[1])
                    elif i == len(map) - 1:
                        destination_ranges.append(to_be_mapped)
                        break
            seeds_location_ranges[-1] = destination_ranges
    return min(row[0] for rows in seeds_location_ranges for row in rows)

if __name__ == '__main__':
    print(f"Part 1: {part1('input.txt')}")
    print(f"Part 2: {part2('input.txt')}")