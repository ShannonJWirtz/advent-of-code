import solution as soln

def read_unique_coords():
    with open('unique_coords.txt') as f:
        lines = [eval('('+line.strip() + ')') for line in f.readlines()]
    return lines

def test_get_overlaps():
    overlaps = soln.get_overlaps(soln.get_inputs('test_input.txt'))
    assert(overlaps[(0,1)][0][0] == 12)
    assert(overlaps[(1,4)][0][0] == 12)

def test_get_coords_part2():
    coords = read_unique_coords()
    t = soln.get_inputs('test_input.txt')
    o = soln.get_overlaps(t)
    coords_to_test = soln.get_coords(t, o, t)[0]
    assert(set(coords) == set(coords_to_test))
    assert(soln.part2(t, o) == 3621)



# def test_get_beacons():
#     assert(soln.get_beacons('test_input.txt') == 79)
