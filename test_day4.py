from day4 import total_enclosing_pairs, convert_assignment_to_range, is_range_within_range, do_ranges_overlap, total_overlapping_pairs

def test_total_enclosing_pairs():
    assert(total_enclosing_pairs('test_inputs/day4.txt') == 2)

def test_convert_assignment_to_range():
    assert(convert_assignment_to_range('3-6') == range(3,7))

def test_is_range_within_range():
    assert(is_range_within_range(range(3,4), range(1,4)) == True)
    assert(is_range_within_range(range(1,4), range(3,4)) == True)
    assert(is_range_within_range(range(1,4), range(5,6)) == False)
    assert(is_range_within_range(range(1,5), range(1,2)) == True)
    assert(is_range_within_range(range(6,6), range(4,7)) == True)

def test_do_ranges_overlap():
    assert(do_ranges_overlap(range(1,4), range(3,6)) == True)
    assert(do_ranges_overlap(range(3,6), range(1,4)) == True)

def test_total_overlapping_pairs():
    assert(total_overlapping_pairs('test_inputs/day4.txt') == 4)



