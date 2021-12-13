import solution
import numpy as np

def test_fold():

    dots = np.array([[1, 0, 0], [0, 0, 1], [1, 0, 1]])

    assert( (solution.fold(dots, ('x', 1)) == np.array([[1], [1], [2]])).all() )
    assert( (solution.fold(dots, ('y', 1)) == np.array([[2, 0, 1]])).all() )

def test_get_dots_after_fold():

    assert(solution.get_dots_after_fold('test_input.txt', 0) == 17)
    assert(solution.get_dots_after_fold('test_input.txt') == 16)
