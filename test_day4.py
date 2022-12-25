from day4 import total_overlapping_pairs, convert_assignment_to_range, is_range_within_range

def test_total_overlapping_pairs():
    assert(total_overlapping_pairs('test_inputs/day4.txt') == 2)

def test_convert_assignment_to_range():
    assert(convert_assignment_to_range('3-6') == range(3,7))

def test_is_range_within_range():
    assert(is_range_within_range(range(3,4), range(1,4)) == True)
    assert(is_range_within_range(range(1,4), range(3,4)) == True)
    assert(is_range_within_range(range(1,4), range(5,6)) == False)
    assert(is_range_within_range(range(1,5), range(1,2)) == True)
    assert(is_range_within_range(range(6,6), range(4,7)) == True)


