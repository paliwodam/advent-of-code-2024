import re

input_file = "Chapter-I/Inputs/Day-3-Input.txt"

def mull_it_over(skip_dont=True):
    result = 0
    with open(input_file) as file:
        data = file.read()

        if not  skip_dont:
            data = re.sub(r"don't\(\)[\s\S]*?do\(\)", '', data)
            data, *_ = data.split("don't()")

        matches = re.findall('mul\(\d+,\d+\)', data)
        for match in matches:
            x, y = re.findall('\d+', match)
            result += int(x) * int(y)
        
        return result

def part1():
    print(mull_it_over())

def part2():
    print(mull_it_over(skip_dont=False))
