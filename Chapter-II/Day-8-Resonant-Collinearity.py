from collections import defaultdict
input_file = "Inputs/Chapter-II/Day-8-Input.txt"

with open(input_file) as file:
    grid = [line.rstrip() for line in file]
    
n, m = len(grid), len(grid[0])

antenas = defaultdict(list)

for x2 in range(n):
    for y2 in range(m):
        if grid[x2][y2] != ".": antenas[grid[x2][y2]].append((x2, y2))


def resonant_collinearity(multiple=False):
    antinodes = set()
    
    for _, ants in antenas.items():
        for x1, y1 in ants:
            for x2, y2 in ants:
                if x1 == x2 and y1 == y2: continue

                if multiple: antinodes |= {(x1, y1), (x2, y2)}

                dx, dy = x1-x2, y1-y2

                x3, y3 = x1 + dx, y1 + dy
                while 0 <= x3 < n and 0 <= y3 < m:
                    antinodes |= {(x3, y3)}
                    x3, y3 = x3 + dx, y3 + dy
                    if not multiple: break

                x3, y3 = x2 - dx, y2 - dy
                while 0 <= x3 < n and 0 <= y3 < m:
                    antinodes |= {(x3, y3)}
                    x3, y3 = x3 - dx, y3 - dy
                    if not multiple: break

    return len(antinodes)

def part1():
    return resonant_collinearity()

def part2():
    return resonant_collinearity(True)
