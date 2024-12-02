
input_file = "Chapter-I/Day-2-Test-Input.txt"
input_file = "Chapter-I/Day-2-Input.txt"

reports = []

with open(input_file) as file:
    for line in file:
        report = [int(x) for x in line.split()]
        reports.append(report)

def check(expression, diff):
    return all(map(expression, diff))

def is_safe(row):
    diff = [row[i] - row[i-1] for i in range(1, len(row))]
    decreasing = check(lambda x: x < 0, diff)
    increasing = check(lambda x: x > 0, diff)
    diff_max_three = check(lambda x: abs(x) <= 3, diff)

    return (decreasing or increasing) and diff_max_three

def calculate_safe_count(diffs):
    safe_count = 0
    for diff in diffs:
        if is_safe(diff): safe_count += 1
    return safe_count

def part1():
    safe_count = 0
    for report in reports:
        if is_safe(report): safe_count += 1
    print(safe_count)

    
def part2():
    safe_count = 0
    n = len(report[0])
    for report in reports:
        if any([is_safe(report[:i] + report[i+1:]) for i in range(n)]): 
            safe_count += 1
    print(safe_count)
part2()