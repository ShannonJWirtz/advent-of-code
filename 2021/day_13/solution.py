import numpy as np

def get_inputs(filename):
    with open(filename) as f:
        lines = f.readlines()

    dots, instructions = [], []
    for line in lines:
        if line[0] in '0123456789':
            dots.append( tuple(int(i) for i in reversed(line.strip().split(','))) )
        if line[0] == 'f':
            instruction = line.strip().split('=')
            instructions.append( (instruction[0][-1], int(instruction[1])) )

    w, h = max(dot[1] for dot in dots) + 1, max(dot[0] for dot in dots) + 1

    dots_array = np.zeros((h, w))

    for dot in dots:
        dots_array[dot[0],dot[1]] = 1

    return dots_array, instructions


dots = np.array([[1, 0, 0], [0, 0, 1], [1, 0, 1]])



def fold(dots_array, instr):

    if instr[0] == 'x':
        left = dots_array[:, :instr[1]]
        right_flipped = dots_array[:,(instr[1] + 1):][:, ::-1]

        width_difference = left.shape[1] - right_flipped.shape[1]
        if width_difference > 0:
            right_flipped = np.pad(right_flipped, [(0,0), (width_difference, 0)], 'constant', constant_values = [(0,0), (0,0)])
        else:
            left = np.pad(left, [(0,0), (-width_difference, 0)], 'constant', constant_values = [(0,0), (0,0)])

        return left + right_flipped

    if instr[0] == 'y':
        up = dots_array[:instr[1], :]
        down_flipped = dots_array[(instr[1] + 1):, :][::-1, :]

        width_difference = up.shape[0] - down_flipped.shape[0]
        if width_difference > 0:
            down_flipped = np.pad(down_flipped, [(width_difference,0), (0, 0)], 'constant', constant_values = [(0,0), (0,0)])
        else:
            up = np.pad(up, [(width_difference,0), (0, 0)], 'constant', constant_values = [(0,0), (0,0)])

        return up + down_flipped

def get_dots_after_fold(filename, n=-1, return_dots_array=False):
    dots_array, instructions = get_inputs(filename)

    for i, instr in enumerate(instructions):
        dots_array = fold(dots_array, instr)
        if n > -1 and i == n:
            break

    dots_array[dots_array > 0] = 1

    if return_dots_array: return dots_array.astype('int')
    else: return np.count_nonzero(dots_array)

if __name__ == '__main__':

    print('First answer is:', get_dots_after_fold('input.txt', 0))
    np.savetxt('dotarr.csv', get_dots_after_fold('input.txt', return_dots_array=True).astype(int), delimiter=',')
    print('Second answer is has been saved to dotarr.csv')
