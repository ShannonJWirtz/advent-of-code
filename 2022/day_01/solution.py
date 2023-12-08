def get_inputs(filename):
    with open(filename) as f: return [line.strip() for line in f.readlines()]

def part1(filename):
    inputs = get_inputs(filename)
    calorie_totals = [0]
    for calorie_number in inputs:
        if calorie_number == '':
            calorie_totals.append(0)
            continue
        else:
            calorie_totals[-1] += int(calorie_number)
    return max(calorie_totals)

def part2(filename):
    inputs = get_inputs(filename)
    calorie_totals = [0]
    for calorie_number in inputs:
        if calorie_number == '':
            calorie_totals.append(0)
            continue
        else:
            calorie_totals[-1] += int(calorie_number)
    calorie_totals.sort(reverse = True)
    return sum(calorie_totals[:3])

if __name__ == '__main__':
    print(f"Part 1: {part1('input.txt')}")
    print(f"Part 2: {part2('input.txt')}")