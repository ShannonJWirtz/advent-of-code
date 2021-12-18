import solution as soln

def test_reduce_snail_number_list():
    assert(soln.reduce_snail_number_list([[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]) ==
           soln.reduce_snail_number_list([[[[0,7],4],[[7,8],[6,0]]],[8,1]]))
    assert(soln.reduce_snail_number_list([ [[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]],  [7,[[[3,7],[4,3]],[[6,3],[8,8]]]]]) ==
           [[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]])
    assert (
        soln.reduce_snail_number_list([[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]], [[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]]) ==
        [[[[7,8],[6,6]],[[6,0],[7,7]]],[[[7,8],[8,8]],[[7,9],[0,6]]]]
    )

def test_magnitude():
    assert(soln.get_magnitude(soln.reduce_snail_number_list([[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]], [[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]])) == 3993)


def test_part2():
    assert(soln.part2('test_input.txt') == 3993)
