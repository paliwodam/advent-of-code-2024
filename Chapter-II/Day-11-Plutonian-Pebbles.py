from math import log10, floor
input_file = "Inputs/Chapter-II/Day-11-Input.txt"

with open(input_file) as file:
    stones = [int(x) for x in file.read().split()]

memo = {}

def blink(stone, blinks):
    if blinks == 0:
        return 1
    
    if stone == 0:
        return blink(1, blinks-1)
    
    if (stone, blinks) not in memo:
        length = floor(log10(stone) + 1)
        if length % 2 == 0:
            left = blink(stone // 10 ** (length // 2), blinks-1) 
            right = blink(stone % 10 ** (length // 2), blinks-1)
            memo[(stone, blinks)] = left + right
        else:
            memo[(stone, blinks)] = blink(stone * 2024, blinks-1)

    return memo[(stone, blinks)]


def part1():
    return sum([blink(stone, 25) for stone in stones])

def part2():
    return sum([blink(stone, 75) for stone in stones])
