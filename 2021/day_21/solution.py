def roll_deterministic_die(current_position):
    new_position = (current_position + 2) % 100 + 1
    sum = current_position + (current_position) % 100 + (current_position + 1) % 100 + 2
    return new_position, sum

def part1(pos1, pos2):
    scores = [0,0]
    positions = [pos1, pos2]
    current_die_position = 1
    rolls = 0

    while all(score < 1000 for score in scores):
            current_die_position, moves = roll_deterministic_die(current_die_position)
            positions[0] = (positions[0] + moves - 1) % 10 + 1
            scores[0] += positions[0]
            rolls += 3
            if scores[0] >= 1000:
                return rolls * scores[1]
            current_die_position, moves = roll_deterministic_die(current_die_position)
            positions[1] = (positions[1] + moves - 1) % 10 + 1
            scores[1] += positions[1]
            rolls += 3
            if scores[1] >= 1000:
                return rolls * scores[0]
    assert(False)

if __name__ == '__main__':
    print('First problem answer:', part1(9, 3))
