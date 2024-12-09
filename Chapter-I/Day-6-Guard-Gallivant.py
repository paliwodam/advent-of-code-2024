input_file = "Inputs/Chapter-I/Day-6-Input.txt"
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

with open(input_file) as file:
    grid = [list(line.rstrip()) for line in file]

n, m = len(grid), len(grid[0])
start = -1, -1

for x in range(n): 
    for y in range(m):
        if grid[x][y] == "^": start = (x, y)

def patrol():
    x, y = start
    dx, dy = directions[0]
    path = set()

    while True:
        if not ((x, y), (dx, dy)) in path:
            path |= {((x, y), (dx, dy))}
        else:
            return path, True
        
        if not (0 <= x + dx < n) or \
           not (0 <= y + dy < m):
            return path, False
        
        while grid[x+dx][y+dy] == "#":
            index = directions.index((dx,dy))
            dx, dy = directions[(index + 1) % 4]
        
        x, y = x+dx, y+dy


def part1():
    path, _ = patrol()
    return len(set(pos for pos, _ in path))
   
def part2():
    count = 0
    path, _ = patrol()
    for (x, y) in set(pos for pos, _ in path):
        tmp, grid[x][y] = grid[x][y], "#"
        _, loop = patrol()
        if loop: count += 1
        grid[x][y] = tmp

    return count
