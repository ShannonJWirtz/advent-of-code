from math import sqrt, floor

def part1(times, records):
    multiplied_times = 1
    for time, record in zip(times, records):
        multiplied_times *= \
        time - 2 * (floor((time - sqrt(time**2 - 4 * record)) / 2)) - 1
    return multiplied_times

def part2(time, record): 
    return part1([time], [record])

if __name__ == '__main__':
    print(f"Part 1: {part1([51, 92, 68, 90], [222, 2031, 1126, 1225])}")
    print(f"Part 2: {part2(51926890, 222203111261225)}")