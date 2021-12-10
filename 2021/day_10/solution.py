from functools import reduce

def get_inputs(filename):
    with open(filename) as f:
        lines = f.readlines()

    return [line.strip() for line in lines]

starts_to_ends = {'{': '}', '[': ']', '(': ')', '<': '>'}
scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
pt2_points = {')': 1, ']': 2, '}': 3, '>': 4}

def get_syntax_error(line, with_stack=False):
    stack = []
    for char in line:
        if char in '{[(<':
            stack.append(char)
        else:
            if starts_to_ends[stack.pop()] != char:
                return char
    if with_stack:
        return ('', stack)
    else:
        return ''

def get_syntax_error_score(inputs):
    return sum(scores.get(get_syntax_error(line), 0) for line in inputs)

def get_incomplete_lines_score(inputs):
     starts_list = [list(reversed(evaluation[1]))
               for evaluation in [get_syntax_error(line, True) for line in inputs]
               if type(evaluation) != str]
     points_list = [[pt2_points[starts_to_ends[start]] for start in starts] for starts in starts_list]
     line_scores = [reduce(lambda x, y: 5 * x + y, points, 0) for points in points_list]
     line_scores.sort()

     return line_scores[int((len(line_scores) - 1) / 2)]

if __name__ == '__main__':

    print('First answer is: ', get_syntax_error_score(get_inputs('input.txt')))
    print('Second answer is: ', get_incomplete_lines_score(get_inputs('input.txt')))
