input_file = "Inputs/Chapter-IV/Day-19-Input.txt"

with open(input_file) as file:
    data = file.read().rstrip()
    towels, designes = data.split("\n\n")

    towels, designes = set(towels.split(", ")), designes.split()
    design_way = {}

def design_ways(design: str):
    if design not in design_way:
        ways = 0
        for towel in towels:
            if design == towel:
                ways += 1
            elif design.startswith(towel):
                ways += design_ways(design[len(towel):])
        design_way[design] = ways
    return design_way[design]
    

def part1():
    return sum(design_ways(design) != 0 for design in designes)

def part2():
    return sum(design_ways(design) for design in designes)

