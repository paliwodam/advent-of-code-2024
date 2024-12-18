import time
from queue import PriorityQueue
input_file = "Inputs/Chapter-III/Day-18-Input.txt"

with open(input_file) as file:
    falling = [tuple(int(x) for x in line.rstrip().split(',')) for line in file]

n = 70
start, end = (0, 0), (n, n)

def in_range(x, y, dx, dy):
    return  0 <= x + dx <= n and 0 <= y + dy <= n

def A_star(bytes): 
    distances = {}
    queue = PriorityQueue()
    queue.put((2 * n, 0, start))
    while not queue.empty():
        _, distance, position = queue.get()

        if position not in distances or distances[position] > distance:
            distances[position] = distance
            
            x, y = position
            for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                if in_range(x, y, dx, dy) and (x+dx, y+dy) not in bytes:
                    h = (n-x-dx + n-y-dy) + (distance+1)
                    queue.put((h, distance+1, (x+dx, y+dy)))
        
        if position == end:
            return distance
    return None

def part1():
    bytes = set(falling[:1024])
    return A_star(bytes)

def part2():
    l, r = 1024, len(falling)-1
    while True:
        m = (r + l) // 2
        if A_star(set(falling[:m])) == None:
            r = m
        else:
            l = m
        
        if r-l <= 1:
            return falling[r-1]
        