from day1 import identify_largest_calories, identify_top_three

def test_identify_largest_calories():
    assert(identify_largest_calories('test_inputs/day1.txt') == 24000)

def test_identify_top_three():
    assert(identify_top_three('test_inputs/day1.txt') == 45000)