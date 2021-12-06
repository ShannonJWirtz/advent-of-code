import solution

def test_get_instructions_from_raw():
    with open('test-input.txt') as f:
        instructions = solution.get_instructions_from_raw(f.readlines())
    assert(instructions == [('forward', 5), ('down', 2), ('up', 1)])

def test_final_position_multipled():
    instructions = [('forward', 2), ('up', 2), ('forward', 3), ('down', 3)]
    assert(solution.final_position_multipled(instructions) == 5)

def test_final_position_multipled_pt2():
    instructions = [('forward', 2), ('up', 2), ('forward', 3), ('down', 3)]
    assert(solution.final_position_multipled_pt2(instructions) == -30)
