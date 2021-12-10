import numpy as np

def get_inputs(filename):
    with open(filename) as f:
        lines = f.readlines()

    return [int(i) for i in lines[0].strip().split(',')]

def get_min_fuel_consumption(inputs):

    inputs.sort()

    optimal_loc = inputs[int((len(inputs) - 1) / 2)]

    fuel_consumption = sum(abs(loc - optimal_loc) for loc in inputs)

    return fuel_consumption

def get_min_fuel_consumption_pt2(inputs):

    mi, ma = min(inputs), max(inputs)

    return min(sum(int(abs(i - j) * (abs(i - j) + 1) / 2) for i in inputs) for j in range(mi, ma + 1))

if __name__ == '__main__':

    print('First problem answer: ', get_min_fuel_consumption(get_inputs('input.txt')))
    print('Second problem answer: ', get_min_fuel_consumption_pt2(get_inputs('input.txt')))
