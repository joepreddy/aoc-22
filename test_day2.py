from day2 import calculate_total_game_score_part_1, convert_shape, evaluate_game, calculate_total_game_score_part_2, build_game

def test_calculate_total_game_score():
    assert(calculate_total_game_score_part_1('test_inputs/day2.txt') == 15)

def test_convert_shape():
    assert(convert_shape('a') == 1)
    assert(convert_shape('x') == 1)
    assert(convert_shape('b') == 2)
    assert(convert_shape('y') == 2)
    assert(convert_shape('c') == 3)
    assert(convert_shape('z') == 3)
    assert(convert_shape('g') == -1)

def test_evaluate_game():
    assert(evaluate_game('A Y') == 8)
    assert(evaluate_game('B X') == 1)
    assert(evaluate_game('C Z') == 6)

def test_calculate_total_game_score_part_2():
    assert(calculate_total_game_score_part_2('test_inputs/day2.txt') == 12)

def test_build_game():
    assert(build_game('A X') == 'a c')
    assert(build_game('A Y') == 'a a')
    assert(build_game('A Z') == 'a b')
    assert(build_game('B X') == 'b a')
    assert(build_game('B Y') == 'b b')
    assert(build_game('B Z') == 'b c')
    assert(build_game('C X') == 'c b')
    assert(build_game('C Y') == 'c c')
    assert(build_game('C Z') == 'c a')