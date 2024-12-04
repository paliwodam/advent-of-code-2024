INPUT_FILE = "Chapter-I/Inputs/Day-4-Input.txt"
DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
XMAS_WORD = "XMAS"

with open(INPUT_FILE) as file:
    grid = [line.rstrip() for line in file]
    n, m = len(grid), len(grid[0])
    
def in_range(i, j):
    return 0 <= i < n and 0 <= j < m

def XMAS(x, y):
    count = 0
    for dx, dy in DIRECTIONS:
        i, j = x+dx, y+dy
        idx = 1
        while in_range(i, j) and idx < len(XMAS_WORD):
            if grid[i][j] != XMAS_WORD[idx]: break
            i, j = i+dx, j+dy
            idx += 1
        if idx == len(XMAS_WORD): count += 1
    return count


def X_MAS(x, y):
    if  x <= 0 or x >= n-1 or y <= 0 or y >= m-1:
        return False
    
    if (grid[x-1][y-1], grid[x+1][y+1]) in [("M", "S"), ("S", "M")] and \
       (grid[x-1][y+1], grid[x+1][y-1]) in [("M", "S"), ("S", "M")]:
        return True
    return False

def search_grid(char, search_function):
    result = 0
    for x in range(n):
        for y in range(m):
            if grid[x][y] == char:
                result += search_function(x, y)

    return result
    
def part1():
    return search_grid("X", XMAS)

def part2():
    return search_grid("A", X_MAS)


print(part1())
print(part2())