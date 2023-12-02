import re

def get_games(lines):
    games = {}
    for line in lines:
        id = int(re.search(r'Game (\d+):', line).group(1))
        rounds_data = re.search(r':(.*)', line).group(1).split(';')
        rounds = []
        for data in rounds_data:
            rounds.append( { entry[1] : int(entry[0]) for entry in re.findall('(\d+) (red|green|blue)', data) } )
        games[id] = rounds
    return games 

def get_part_1_sum(lines):
    games = get_games(lines)
    return sum(id for id, game in games.items() if all(round.get('red',0) <= 12 and round.get('green',0) <= 13 and round.get('blue',0) <= 14 for round in game))

def get_part_2_sum(lines):
    games = get_games(lines)
    game_minimums = [
        {'red': max(round.get('red',0) for round in game), 
         'green': max(round.get('green',0) for round in game), 
         'blue': max(round.get('blue',0) for round in game)}
        for game in games.values()
    ]
    return sum(game_min['red'] * game_min['green'] * game_min['blue'] for game_min in game_minimums)

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = tuple(line.strip() for line in f.readlines())
    print('Solution 1 is {}'.format(get_part_1_sum(lines)))
    print('Solution 2 is {}'.format(get_part_2_sum(lines)))