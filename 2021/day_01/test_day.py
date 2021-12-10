import solution

def test_depth_sum():
    assert(solution.depth_sum([1,2,-1,-3,1]) == 2)

    assert(solution.depth_sum([1,1]) == 0)

def test_windowed_depth_sum():
    assert(solution.windowed_depth_sum([1,2,-1,-3,1]) == 0)

    assert(solution.windowed_depth_sum([1,1,1,2]) == 1)
