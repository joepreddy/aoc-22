
from utils import readfile

def identify_largest_calories(input):
    list = readfile(input)
    calories = 0
    highestCalories = 0
    for item in list:
        if not item == '\n':
            calories += int(item)
        else :
            if calories > highestCalories:
                highestCalories = calories
            calories = 0
    return highestCalories

def identify_top_three(input):
    list = readfile(input)
    calories = 0
    total_calories = []

    for item in list:
        if not item == '\n':
            calories += int(item)
        else:
            total_calories.append(calories)
            calories = 0
    total = 0
    for i in range(3):
        curr_max = max(total_calories)
        total += curr_max
        total_calories.remove(curr_max)
    return total
        


        

print(identify_largest_calories('inputs/day1.txt'))
print(identify_top_three('inputs/day1.txt'))