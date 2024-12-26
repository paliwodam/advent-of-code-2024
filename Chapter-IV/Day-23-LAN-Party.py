from collections import defaultdict
input_file = "Inputs/Chapter-IV/Day-23-Input.txt"

connections = defaultdict(list)

with open(input_file) as file:
    for line in file.readlines():
        left, right = line.strip().split("-")
        connections[left].append(right)
        connections[right].append(left)

def getTriples(starts_with_t=False):
    triples = set()
    for x, connected in connections.items():
        for y in connected:
            for z in connections[y]:
                if z in connected and (not starts_with_t or x.startswith("t")):
                    triples.add(frozenset([x, y, z]))
    return triples

def part1():
    return len(getTriples(starts_with_t=True))

def part2():
    cliques = getTriples()
    while True:
        extended = set()
        for clique in cliques:
            x = next(iter(clique))
            for y in connections[x]:
                valid = y in clique
                for z in clique:
                    if y not in connections[z]: valid = False
                if valid: extended |= {frozenset(list(clique) + [y])}
        if len(extended) == 0: break
        cliques = extended
    return ",".join(sorted(*cliques))