from collections import Counter

def get_inputs(filename):
   with open(filename) as f:
       lines = f.readlines()
   return tuple(
       tuple(tuple([int(i) for i in part.split(',')])
             for part in line.split(' -> '))
       for line in lines)

def get_overlap_number(inputs):
    line_points = []

    for line in inputs:

        if line[0][0] == line[1][0]:
            second_higher = line[1][1] > line[0][1]
            for point in ((line[0][0], i) for i in range(line[0][1],line[1][1] + (-1, 1)[second_higher], (-1, 1)[second_higher])):
                line_points.append(point)

        if line[0][1] == line[1][1]:
            second_higher = line[1][0] > line[0][0]
            for point in ((i, line[0][1]) for i in range(line[0][0], line[1][0] + (-1, 1)[second_higher], (-1, 1)[second_higher])):
                line_points.append(point)

    return(len([_ for _, count in Counter(line_points).items() if count > 1]))

def get_overlap_number_pt2(inputs):
    line_points = []

    for line in inputs:

        if line[0][0] == line[1][0]:
            second_higher = line[1][1] > line[0][1]
            for point in ((line[0][0], i) for i in range(line[0][1],line[1][1] + (-1, 1)[second_higher], (-1, 1)[second_higher])):
                line_points.append(point)
        elif line[0][1] == line[1][1]:
            second_higher = line[1][0] > line[0][0]
            for point in ((i, line[0][1]) for i in range(line[0][0], line[1][0] + (-1, 1)[second_higher], (-1, 1)[second_higher])):
                line_points.append(point)
        else:
            second_horizontal_higher = line[1][0] > line[0][0]
            second_vertical_higher = line[1][1] > line[0][1]

            horizontal_points = range(line[0][0], line[1][0] + (-1, 1)[second_horizontal_higher], (-1, 1)[second_horizontal_higher])
            vertical_points = range(line[0][1],line[1][1] + (-1, 1)[second_vertical_higher], (-1, 1)[second_vertical_higher])

            for point in zip(horizontal_points, vertical_points):
                line_points.append(point)

    return(len([_ for _, count in Counter(line_points).items() if count > 1]))

if __name__ == '__main__':
    print('First problem answer: ', get_overlap_number(get_inputs('input.txt')))
    print('Second problem answer: ', get_overlap_number_pt2(get_inputs('input.txt')))
