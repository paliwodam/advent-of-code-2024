input_file = "Inputs/Grand-Finale/Day-25-Input.txt"

with open(input_file) as file:
    locks_and_keys = file.read().rstrip().split("\n\n")
    locks, keys = [], []
    n, m = 7, 5

def get_heights(e):
    heights = []
    for j in range(m):
        height = 0
        for i in range(1, n):
            if e[i][j] == ".": break
            height += 1
        heights.append(height)
    return heights

def finale():
    for e in locks_and_keys:
        e = e.split("\n")
        if e[0][0] == "#": locks.append(get_heights(e))
        else: keys.append(get_heights(list(reversed(e))))   

    not_overlap = 0
    for l in locks:
        for k in keys:
            overlap = False
            for i in range(m):
                if l[i] + k[i] > n-2:
                    overlap = True
            if not overlap: 
                not_overlap += 1
    return not_overlap