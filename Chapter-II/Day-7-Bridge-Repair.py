input_file = "Inputs/Chapter-II/Day-7-Input.txt"

with open(input_file) as file:
    lines = [line.rstrip() for line in file]
    equations = []

    for line in lines:
        expected, values = line.split(":")
        equations.append((int(expected), [int(x) for x in values.split()]))


def calibration_result(expected, values, concatenation=False):
    memo = {(values[0], 0): expected}

    def get(result, index):
        if result < 0 or index < 0:
            return 0
        
        key = (result, index)
        value = values[index]

        if key not in memo:
            memo[key] = get(result - value, index-1)

            if result % value == 0 and not memo[key]:
                memo[key] = memo[key] or get(result // value, index-1)

            if concatenation and str(result).endswith(str(value)):
                n = 10 ** len(str(value))
                memo[key] = memo[key] or get(result // n, index-1)

        return memo[key]

    return get(expected, len(values)-1)

def part1():
    return sum(calibration_result(e, v) for e, v in equations)

def part2():
    return sum(calibration_result(e, v, True) for e, v in equations)
