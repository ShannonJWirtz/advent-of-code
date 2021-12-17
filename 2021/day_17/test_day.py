import solution as soln

def test_get_highest_possible_point():
    assert(45 == soln.get_highest_possible_point(20, 30, -10, -5))

def test_get_velocities_count():
    assert(112 == soln.get_velocities_count(20, 30, -10, -5))
