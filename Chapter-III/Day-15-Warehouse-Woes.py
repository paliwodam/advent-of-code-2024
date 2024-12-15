import itertools 
input_file = "Inputs/Chapter-III/Day-15-Input.txt"

def expand(x):
    if x == "#":
        return ["#", "#"]
    if x == "O":
        return ["[", "]"]
    return [x, "."]

with open(input_file) as file:
    data = file.read().rstrip()
    warehouse, moves = data.split("\n\n")

    warehouse = [list(x) for x in warehouse.split()]
    extended_warehouse = [list(itertools.chain.from_iterable(map(expand, x))) for x in warehouse]
    moves = "".join(moves.split("\n"))

def move(x, y, dx, dy, w):
    next_field = w[x+dx][y+dy]

    if next_field == "#": return
    if next_field in ("O", "[", "]"): move(x+dx, y+dy, dx, dy, w)
    if next_field == "[" and dy == 0: move(x+dx, y+dy+1, dx, dy, w)
    if next_field == "]" and dy == 0: move(x+dx, y+dy-1, dx, dy, w)

    w[x][y], w[x+dx][y+dy] = w[x+dx][y+dy], w[x][y]

def can_move(x, y, dx, dy, w):
    next_field = w[x+dx][y+dy] 

    if next_field == "#": return False
    if next_field == ".": return True

    can_move_next = can_move(x+dx, y+dy, dx, dy, w)

    if next_field == "[" and dy == 0: return can_move_next and can_move(x+dx, y+dy+1, dx, dy, w)
    if next_field == "]" and dy == 0: return can_move_next and can_move(x+dx, y+dy-1, dx, dy, w)

    return can_move_next

def warehouse_woes(extended=False):
    moves_map = {"^": (-1, 0), "<": (0, -1), "v": (1, 0), ">": (0, 1)}
    lx, ly = len(warehouse), len(warehouse[0])

    if extended:
       ly, c, w= ly * 2, "[", extended_warehouse
    else:
       w, c = "O", warehouse

    x, y = next((x, y) for x in range(lx) for y in range(ly) if w[x][y] == "@")    

    for m in moves:
        dx, dy = moves_map[m]
        if can_move(x, y, dx, dy, w):
            move(x, y, dx, dy, w)
            x, y = x + dx, y + dy

    return sum(x * 100 + y for x in range(lx) for y in range(ly) if w[x][y] == c)
    
def part1():
    return warehouse_woes()

def part2():
    return warehouse_woes(extended=True)
