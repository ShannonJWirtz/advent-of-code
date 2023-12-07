from collections import Counter

CARD_ORDER_PART1 = '23456789TJQKA'
CARD_ORDER_PART2 = 'J23456789TQKA'

def read_inputs(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]

def part1(filename):
    lines = read_inputs(filename)
    hand_values_and_bids = []
    for line in lines:
        hand, bid = line.split()
        bid = int(bid)
        counts = Counter(hand)
        if max(counts.values()) == 5:
            primary_value = 6
        elif max(counts.values()) == 4:
            primary_value = 5
        elif max(counts.values()) == 3 and any(value == 2 for value in counts.values()):
            primary_value = 4
        elif max(counts.values()) == 3:
            primary_value = 3
        elif sum(value == 2 for value in counts.values()) == 2:
            primary_value = 2
        elif max(counts.values()) == 2:
            primary_value = 1
        else:
            primary_value = 0
        secondary_value = tuple(CARD_ORDER_PART1.index(card) for card in hand)
        hand_values_and_bids.append(((primary_value,) + secondary_value, bid))
    hand_values_and_bids.sort(key = lambda x: x[0])
    return sum(hand_value_and_bid[1] * (rank + 1) 
               for rank, hand_value_and_bid
               in enumerate(hand_values_and_bids))

def part2(filename):
    lines = read_inputs(filename)
    hand_values_and_bids = []
    for line in lines:
        hand, bid = line.split()
        bid = int(bid)
        counts = Counter(hand)
        max_counts_not_joker = max([v for k, v in counts.items() if k != 'J'], default=0)
        if max_counts_not_joker + counts['J'] == 5:
            primary_value = 6
        elif max_counts_not_joker + counts['J'] == 4:
            primary_value = 5
        elif max(counts.values()) == 3 and any(value == 2 for value in counts.values()) or \
            counts['J'] == 1 and sum(value == 2 for value in counts.values()) == 2:
            primary_value = 4
        elif max_counts_not_joker + counts['J'] == 3:
            primary_value = 3
        elif sum(value == 2 for value in counts.values()) == 2:
            primary_value = 2
        elif max_counts_not_joker + counts['J'] == 2:
            primary_value = 1
        else:
            primary_value = 0
        secondary_value = tuple(CARD_ORDER_PART2.index(card) for card in hand)
        hand_values_and_bids.append(((primary_value,) + secondary_value, bid))
    hand_values_and_bids.sort(key = lambda x: x[0])
    return sum(hand_value_and_bid[1] * (rank + 1) 
               for rank, hand_value_and_bid
               in enumerate(hand_values_and_bids))

if __name__ == '__main__':
    print(f"Part 1: {part1('input.txt')}")
    print(f"Part 2: {part2('input.txt')}")
