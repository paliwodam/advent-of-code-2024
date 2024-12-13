input_file = "Inputs/Chapter-II/Day-12-Input.txt"

with open(input_file) as file:
    grid = [list(line.rstrip()) for line in file]
    n, m = len(grid), len(grid[0])

def top_perimeter(x, y):
    return x == 0 or grid[x-1][y] != grid[x][y]

def left_perimeter(x, y):
    return y == 0 or grid[x][y-1] != grid[x][y]

def bottom_perimeter(x, y):
    return x == n-1 or grid[x+1][y] != grid[x][y]

def right_perimeter(x, y):
    return y == m-1 or grid[x][y+1] != grid[x][y]   

def concave_top_right(x, y):
    if not (x < n-1 and y > 0): return False
    return grid[x][y] == grid[x+1][y] == grid[x][y-1] != grid[x+1][y-1]

def concave_top_left(x, y):
    if not (x < n-1 and y < m-1): return False
    return grid[x][y] == grid[x+1][y] == grid[x][y+1] != grid[x+1][y+1]

def concave_bottom_right(x, y):
    if not (x > 0 and y > 0): return False
    return grid[x][y] == grid[x-1][y] == grid[x][y-1] != grid[x-1][y-1]

def concave_bottom_left(x, y):
    if not(x > 0 and y < m-1): return False
    return grid[x][y] == grid[x-1][y] == grid[x][y+1] != grid[x-1][y+1]

def perimeters_x_y(x, y):
    return sum([
        top_perimeter(x, y), 
        left_perimeter(x, y), 
        bottom_perimeter(x, y), 
        right_perimeter(x, y)
    ])

def corners_x_y(x, y):
    return sum([
        top_perimeter(x, y) and left_perimeter(x, y),
        top_perimeter(x, y) and right_perimeter(x, y),
        bottom_perimeter(x, y) and left_perimeter(x, y),
        bottom_perimeter(x, y) and right_perimeter(x, y),
        concave_top_right(x, y),
        concave_top_left(x, y),
        concave_bottom_right(x, y),
        concave_bottom_left(x, y)
    ])

def group_price(i, j, visited, discount):
    if (i, j) not in visited:
        perimeters, corners, area = 0, 0, 0
        queue = [((i, j))]
        while queue:
            x, y = queue.pop()
            if (x, y) in visited: continue

            corners += corners_x_y(x, y)
            perimeters += perimeters_x_y(x, y)
            area += 1

            visited |= {(x, y)}

            if x < n-1 and grid[x+1][y] == grid[x][y]:
                queue.append((x+1, y))
            if y < m-1 and grid[x][y+1] == grid[x][y]:
                queue.append((x, y+1))
            if x > 0 and grid[x-1][y] == grid[x][y]:
                queue.append((x-1, y))
            if y > 0 and grid[x][y-1] == grid[x][y]:
                queue.append((x, y-1))
        
        return area * corners if discount else area * perimeters
    return 0

def garden_groups(discount=False):
    visited = set()
    return sum([sum([group_price(i, j, visited, discount) for j in range(m)]) for i in range(m)])

def part1():
    return garden_groups()

def part2():
    return garden_groups(discount=True)
