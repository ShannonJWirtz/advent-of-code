import solution

def test_get_safest_path_and_score_astar():
    path_to_test, risk_score_to_test = solution.get_safest_path_and_score_astar('test_input.txt')
    path1 = [
        (0,0), (1,0), (2,0), (2,1), (2,2), (2,3), (2,4), (2,5), (2,6),
        (3,6), (3,7), (4,7), (5,7), (5,8), (6,8), (7,8), (8,8), (8,9), (9,9)
    ]
    path2 = [
        (0,0), (1,0), (2,0), (2,1), (2,2), (2,3), (2,4), (2,5), (2,6),
        (3,6), (3,7), (4,7), (4,8), (5,8), (6,8), (7,8), (8,8), (8,9), (9,9)
    ]
    risk_score = 40
    assert(path_to_test == path1 or path_to_test == path2)
    assert(risk_score_to_test == risk_score)

def test_get_safest_path_and_score_astar_pt2():
    path_to_test, risk_score_to_test = solution.get_safest_path_and_score_astar('test_input.txt', True)
    risk_score = 315
    assert(risk_score_to_test == risk_score)
