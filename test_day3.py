from day3 import get_sum_common_items, split_rucksack, find_duplicates, score_chars, get_sum_badges, split_rucksacks_into_groups, find_common_item_in_group

def test_get_sum_common_items():
    assert(get_sum_common_items('test_inputs/day3.txt') == 157)

def test_split_rucksack():
    assert(split_rucksack('abcdef') == ['abc','def'])

def test_find_duplicates():
    assert(find_duplicates(['abc', 'dha']) == {'a'})

def test_score_chars():
    assert(score_chars(['e', 'E']) == 36)

def test_get_sum_badges():
    assert(get_sum_badges('test_inputs/day3.txt') == 70)

def test_split_rucksacks_into_groups():
    assert(split_rucksacks_into_groups(['a','b','c','d','e','f']) == [['a','b','c'],['d','e','f']])

def test_find_common_item_in_group():
    assert(find_common_item_in_group([['a','b','c'], ['d', 'e', 'c'], ['c', 'f', 'g']]) == 'c')
