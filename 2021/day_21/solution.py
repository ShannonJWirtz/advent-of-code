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
from collections import defaultdict
def get_dist(n):
    positions = defaultdict(int)
    positions[0] = 1
    for _ in range(n):
        for i in range(1, 4, 1):
            tmp_positions = {}
            for position, count in positions.items():
                tmp_positions[position + i] = count
            for i, count in tmp_positions.items():
                positions[i] += count
    return positions
position, i = 10, 2
(position+i-1)%10 + 1
def get_possible_scores(start, steps):
    position_dict = lambda : dict(positions=defaultdict(int), win=0)
    steps_data = [defaultdict(position_dict)]
    steps_data[-1][0]['positions'][start] = 1
    for i in range(1,steps+1,1):
        previous_step = steps_data[-1]
        tmp_step = defaultdict(position_dict)
        for score, positions in previous_step.items():
            for position, count in positions['positions'].items():
                for i in range(1, 4, 1):
                    next_position = (position+i-1)%10 + 1
                    tmp_step[score+next_position]['positions'][next_position] += count
                    if score < 21 <= score+next_position:
                        tmp_step[score+next_position]['win'] += count
        steps_data.append(tmp_step)
    return steps_data


def part2(start1, start2):
    player_1 = get_possible_scores(start1,21)
    player_2 = get_possible_scores(start2,21)
    player_1_wins, player_2_wins = 0
    for pos_scores_1, pos_scores_2 in zip(player_1, player_2):











if __name__ == '__main__':
    print('First problem answer:', part1(9, 3))
