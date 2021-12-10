
def get_inputs(filename):
    with open(filename) as f:
        lines = f.readlines()

    return [line.strip() for line in lines]

starts_to_ends = {'{': '}', '[': ']', '(': ')', '<': '>'}
scores = {')': 3, ']': 57, '}': 1197, '>': 25137}

def get_syntax_error(line):
    stack = []
    for char in line:
        if char in '{[(<':
            stack.append(char)
        else:
            last_opener = stack.pop()
            if starts_to_ends[last_opener] != char:
                return char
    return ''

def get_syntax_error_score(inputs):
    return sum(scores.get(get_syntax_error(line), 0) for line in inputs)

if __name__ == '__main__':

    print('First answer is: ', get_syntax_error_score(get_inputs('input.txt')))
