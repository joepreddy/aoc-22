from utils import readfile_strip

def calculate_total_game_score_part_1(file):
    games = readfile_strip(file)
    total_score = 0
    for game in games:
        total_score += evaluate_game(game)
    return total_score

def calculate_total_game_score_part_2(file):
    lines = readfile_strip(file)
    total_score = 0
    for line in lines:
        game = build_game(line)
        total_score += evaluate_game(game)
    return total_score

def evaluate_game(game):
    opponent_turn = convert_shape(game.split(" ")[0].lower())
    friendly_turn = convert_shape(game.split(" ")[1].lower())
    
    game_score = friendly_turn

    if friendly_turn == opponent_turn:
        game_score += 3
    elif friendly_turn == 1: # if rock
        if opponent_turn == 3: # if other scissors
            game_score += 6 # win
    elif friendly_turn == 2: # if paper
        if opponent_turn == 1: # if other rock
            game_score += 6 # win
    elif friendly_turn == 3:
        if opponent_turn == 2:
            game_score += 6
    
    return game_score
    
def convert_shape(shape):
    if shape == 'a' or shape == 'x':
        return 1
    elif shape == 'b' or shape == 'y':
        return 2
    elif shape == 'c' or shape == 'z':
        return 3
    else:
        return -1

def build_game(turn):
    opponent_turn = turn.split(" ")[0].lower()
    strategy = turn.split(" ")[1].lower()
    friendly_turn = ''

    if strategy == 'y': # draw
        friendly_turn = opponent_turn
    elif strategy == 'x': # lose
        if opponent_turn == 'a':
            friendly_turn = 'c'
        elif opponent_turn == 'b':
            friendly_turn = 'a'
        elif opponent_turn == 'c':
            friendly_turn = 'b'
    elif strategy == 'z': #win
        if opponent_turn == 'a':
            friendly_turn = 'b'
        if opponent_turn == 'b':
            friendly_turn = 'c'
        if opponent_turn == 'c':
            friendly_turn = 'a'
    
    return f'{opponent_turn} {friendly_turn}'



print(calculate_total_game_score_part_1('inputs/day2.txt'))
print(calculate_total_game_score_part_2('inputs/day2.txt'))