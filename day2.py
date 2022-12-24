from utils import readfile_strip

def calculate_total_game_score(file):
    games = readfile_strip(file)
    total_score = 0
    for game in games:
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


print(calculate_total_game_score('inputs/day2.txt'))