import solution as soln


def test_def_roll_deterministic_die():
    pos_to_test, sum_to_test = soln.roll_deterministic_die(1)
    assert(pos_to_test == 4)
    assert(sum_to_test == 6)
    pos_to_test, sum_to_test = soln.roll_deterministic_die(99)
    assert(pos_to_test == 2)
    assert(sum_to_test == 200)

def test_part1():
    assert(soln.part1(4,8) == 739785)
