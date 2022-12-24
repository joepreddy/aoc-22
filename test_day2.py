from day2 import calculate_total_game_score, convert_shape, evaluate_game

def test_calculate_total_game_score():
    assert(calculate_total_game_score('test_inputs/day2.txt') == 15)

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