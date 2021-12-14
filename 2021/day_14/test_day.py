import solution
from collections import Counter

def test_get_inputs():

    template, instructions = solution.get_inputs('test_input.txt')
    assert(template == 'NNCB')
    assert(
        instructions == {
        'CH': 'B',
        'HH': 'N',
        'CB': 'H',
        'NH': 'C',
        'HB': 'C',
        'HC': 'B',
        'HN': 'C',
        'NN': 'C',
        'BH': 'H',
        'NC': 'B',
        'NB': 'B',
        'BN': 'B',
        'BB': 'N',
        'BC': 'B',
        'CC': 'N',
        'CN': 'C'}
    )

def test_part1():
    assert(solution.part1('test_input.txt') == 1588)

def test_get_next_paircounts():
    template, instructions = solution.get_inputs('test_input.txt')
    template = '~' + template + '*'
    template_after_step1 = '~' + 'NCNBCHB' + '*'
    paircounts = Counter(template[i:i+2] for i in range(len(template) - 1))
    paircounts_after_step1 = Counter(template_after_step1[i:i+2] for i in range(len(template_after_step1) - 1))
    test_paircounts = solution.get_next_paircounts(paircounts, instructions)

    assert(test_paircounts == paircounts_after_step1)

def test_part2():
    assert(solution.part2('test_input.txt', 1) == 1)
    assert(solution.part2('test_input.txt') == 1588)
