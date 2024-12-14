import re
input_file = "Inputs/Chapter-III/Day-14-Input.txt"

with open(input_file) as file:
    robots = [line.rstrip() for line in file]
    for i in range(len(robots)):
        x, y, vx, vy = map(int, re.findall(r'-?\d+', robots[i]))
        robots[i] = ((x, y), (vx, vy))
        
X, Y = 101, 103

def move(seconds, visuals_only=False):
    posiions = set() if visuals_only else []
    for robot in robots:
        (x, y), (vx, vy) = robot
        x, y = (x+vx*seconds) % X, (y+vy*seconds) % Y
        posiions.add((x,y)) if visuals_only else posiions.append((x,y))

    return posiions

def part1():
    positions=move(100)
    hx, hy = X // 2, Y // 2
    q1, q2, q3, q4 = 0, 0, 0, 0

    for x, y in positions:
        if x < hx and y < hy: q1 += 1
        if x < hx and y > hy: q2 += 1
        if x > hx and y < hy: q3 += 1
        if x > hx and y > hy: q4 += 1

    return q1 * q2 * q3 * q4

def part2():
    positions = move(7603)
    for i in range(X):
        for j in range(Y):
            if (j, i) in positions:
                print("█", end="")
            else:
                print(" ", end="")
        print()
    return 7603
