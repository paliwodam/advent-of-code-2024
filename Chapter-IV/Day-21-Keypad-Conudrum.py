from collections import Counter, defaultdict
input_file = "Inputs/Chapter-IV/Day-21-Input.txt"

codes = open(input_file).read().split("\n")

numeric = {c: (i % 3, i // 3) for i, c in enumerate("789456123 0A")}
directional = {c: (i % 3, i // 3) for i, c in enumerate(" ^A<v>")}


def extend_steps(keypad, steps_str, steps_dict, i=1):
    x, y = keypad["A"]
    bx, by = keypad[" "]

    for step in steps_str:
        nx, ny = keypad[step]
        new_step = ""
        if nx < x:
            new_step += "<" * (x - nx)
        if ny > y:
            new_step += "v" * (ny - y)
        if ny < y:
            new_step += "^" * (y - ny)
        if nx > x:
            new_step += ">" * (nx - x)

        if (nx == bx and y == by) or (ny == by and x == bx):
            new_step = new_step[::-1]
        
        steps_dict[new_step + "A"] += i
        x, y = nx, ny
    
    return steps_dict

def keypad_conudrum(n):
    result = 0
    for code in codes:
        steps = extend_steps(numeric, code, defaultdict(int))
        for i in range(n+1):
            new_steps = defaultdict(int)
            for step, i in steps.items():
                extend_steps(directional, step, new_steps, i)
            steps = new_steps
        result += sum(steps.values()) * int(code[:3])
    return result


def part1():
    return keypad_conudrum(2)

def part2():
    return keypad_conudrum(25)
