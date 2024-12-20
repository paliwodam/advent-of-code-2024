from collections import defaultdict
input_file = "Inputs/Chapter-IV/Day-20-Input.txt"

with open(input_file) as file:
    track = [list(line.rstrip()) for line in file]
    n, m = len(track), len(track[0])

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

S = next((i, r.index("S")) for i, r in enumerate(track) if "S" in r)
picoseconds = {S: 0}
todo = [S]
for x, y in todo:
    for nx, ny in [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]:
        if track[nx][ny] != "#" and (nx, ny) not in picoseconds:
            picoseconds[(nx, ny)] = picoseconds[(x, y)] + 1
            todo += [(nx, ny)]

cheats_2 = defaultdict(int)
cheats_20 = defaultdict(int)

for x1, y1 in picoseconds:
    for x2, y2 in picoseconds:
        if (x1, y1) == (x2, y2): continue
        l = abs(x1-x2) + abs(y1-y2)
        ps1, ps2 = picoseconds[(x1, y1)], picoseconds[(x2, y2)]
        if l == 2: 
            cheats_2[ps2-ps1-l] += 1
        if l <= 20:
            cheats_20[ps2-ps1-l] += 1

def part1():
    return sum(v for k, v in cheats_2.items() if k >= 100)

def part2():
    return sum(v for k, v in cheats_20.items() if k >= 100)
