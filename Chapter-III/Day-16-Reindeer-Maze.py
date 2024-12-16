from collections import defaultdict
from queue import PriorityQueue
input_file = "Inputs/Chapter-III/Day-16-Input.txt"

with open(input_file) as file:
    maze = [list(line.rstrip()) for line in file]
    n, m = len(maze), len(maze[0])
    start, end = (n-2, 1), (1, m-2)

def reindeer_maze():
    scores = {}
    is_from = defaultdict(list)

    race = PriorityQueue()
    race.put((0, start, (0, 1), None))
 

    while not race.empty():
        score, position, direction, prev = race.get()

        if (position, direction) not in scores:
            is_from[(position, direction)].append(prev)
            scores[(position, direction)] = score
            (x, y), (dx, dy) = position, direction

            if maze[x+dx][y+dy] != "#":
                race.put((score+1, (x+dx, y+dy), (dx, dy), ((x, y), (dx, dy))))
            
            if maze[x+dy][y+dx] != "#":
                race.put((score+1001, (x+dy, y+dx), (dy, dx), ((x, y), (dx, dy))))
                
            if maze[x-dy][y-dx] != "#":
                race.put((score+1001, (x-dy, y-dx), (-dy, -dx), ((x, y), (dx, dy))))

        elif scores[(position, direction)] == score:
            is_from[(position, direction)].append(prev)
        
        if position == end:
            return score, is_from, (end, direction)
            

def part1():
    score, _, _ = reindeer_maze()
    return score

def part2():
    _, is_from, key = reindeer_maze()
    seats, queue = set(), [key]

    while queue:
        position, direction = queue.pop()
        seats |= {position}
        for best in is_from[(position, direction)]:
            if best is not None: queue.append(best)

    return len(seats)

