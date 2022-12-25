from utils import readfile_strip, split

def get_sum_common_items(file):
    total = 0
    rucksacks = readfile_strip(file)
    for rucksack in rucksacks:
        split_sack = split_rucksack(rucksack)
        total += score_chars(find_duplicates(split_sack))
    return total

def split_rucksack(rucksack):
    first = rucksack[:len(rucksack)//2]
    second = rucksack[len(rucksack)//2 :]
    return [first, second]

def find_duplicates(split_sack):
    matches = set()
    for char in split_sack[0]:
        if char in split_sack[1]:
            matches.add(char)
    return matches

def score_chars(chars):
    score = 0
    for char in chars:
        if char.isupper():
            score += (ord(char) - 38)
        else:
            score += (ord(char) - 96)
    return score

def get_sum_badges(file):
    total = 0
    rucksacks = readfile_strip(file)
    groups = split_rucksacks_into_groups(rucksacks)
    for group in groups:
        badge = find_common_item_in_group(group)
        total += score_chars([badge])
    return total

def split_rucksacks_into_groups(rucksacks):
    return list(split(rucksacks, 3))

def find_common_item_in_group(group):
    for item in group[0]:
        if item in group[1] and item in group[2]:
            return item


print(get_sum_common_items('inputs/day3.txt'))
print(get_sum_badges('inputs/day3.txt'))
