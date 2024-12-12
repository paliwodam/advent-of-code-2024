from collections import defaultdict
input_file = "Inputs/Chapter-II/Day-10-Input.txt"

with open(input_file) as file:
    grid = [list(line.rstrip()) for line in file]
    grid = [[int(x) if x != "." else -1 for x in line] for line in grid]
    n, m = len(grid), len(grid[0])


def hoof_it(distinck_trails = False):
    queue = []
    visited = defaultdict(set)

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0 and distinck_trails:
                queue.append(((i, j), ((i, j),)))
            elif grid[i][j] == 0:
                queue.append(((i, j), (i, j)))

    while queue:
        (x, y), path = queue.pop()

        if distinck_trails:
            path = path + ((x, y),)
        if path in visited[(x, y)]: continue

        visited[(x, y)] |= { path }
        
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            if 0 <= x+dx < n and 0 <= y+dy < m:
                if grid[x+dx][y+dy] == grid[x][y] + 1:
                    queue.append(((x+dx, y+dy), path))
    
    return sum([len(v) for (x, y), v in visited.items() if grid[x][y] == 9])


def part1():
    return hoof_it()

def part2():
    return hoof_it(distinck_trails=True)
