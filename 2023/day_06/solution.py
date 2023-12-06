from functools import reduce

def part1(times, records):
    return reduce(
        lambda x, y: x*y,
        (len([press_time * (time - press_time)
             for press_time in range(1, time)
             if press_time * (time - press_time) > record])
             for time, record in zip(times, records)))

def part2(time, record): 
    return part1([time], [record])

if __name__ == '__main__':
    print(f"Part 1: {part1([51, 92, 68, 90], [222, 2031, 1126, 1225])}")
    print(f"Part 2: {part2(51926890, 222203111261225)}")