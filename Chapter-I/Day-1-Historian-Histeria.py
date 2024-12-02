
from collections import Counter
input_file = "Chapter-I/Day-1-Input.txt"

left_list = []
right_list = []
with open(input_file) as file:
    for line in file:
        left, right = line.rstrip().split()
        left_list.append(int(left))
        right_list.append(int(right))

def part1():
    left_list.sort()
    right_list.sort()

    distance = sum(map(lambda x: abs(x[0]-x[1]), zip(left_list, right_list)))
    print(distance)

def part():
    cnt = Counter(right_list)
    similarity_score = sum(map(lambda x: x * cnt[x], left_list))
    print(similarity_score)