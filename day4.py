from utils import readfile_strip

def total_overlapping_pairs(file):
    total = 0
    lines = readfile_strip(file)
    for line in lines:
        pair = line.split(",")
        range1, range2 = convert_assignment_to_range(pair[0]), convert_assignment_to_range(pair[1])
        if is_range_within_range(range1, range2):
            total += 1
    return total


def convert_assignment_to_range(assignment):
    start, end = assignment.split("-")[0], assignment.split("-")[1]
    return range(int(start), int(end)+1) # ranges apparently don't include the end

def is_range_within_range(range1, range2):
    if(len(range1) == 0): # Deal with ranges like (6,6)
        if range1.start in range2:
            return True
    elif(len(range2) == 0):
        if range2.start in range1:
            return True
    return ((range1.start in range2 and range1[-1] in range2) or (range2.start in range1 and range2[-1] in range1))

print(total_overlapping_pairs('inputs/day4.txt'))