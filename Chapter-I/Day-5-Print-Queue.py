from collections import defaultdict
input_file = "Inputs/Chapter-I/Day-5-Input.txt"

    
with open(input_file) as file:
    data = file.read()
    rules, updates = data.split("\n\n")
    rules, updates = rules.split(), updates.split()

    before = defaultdict(set)

    for rule in rules:
        x, y = rule.split("|")
        before[y].add(x)

def print_queue(fix_order=False):
    result = 0
    for update in updates:
        update = update.split(",")
        update_pages = set(update)
        order = sorted(update, key=lambda x: len(update_pages.intersection(before[x])))
        if order == update and not fix_order:
            result += int(order[len(order) // 2])
        if order != update and fix_order:
            result += int(order[len(order) // 2])
    return result

def part1():
    print(print_queue())

def part2():
    print(print_queue(True))