from collections import defaultdict
input_file = "Inputs/Chapter-IV/Day-24-Input.txt"

with open(input_file) as file:
    data = file.read().rstrip()
    init_values, equations = data.split("\n\n")
    init_values, equations = init_values.split("\n"), equations.split("\n")

n = len(equations)
operators_map = {"AND": lambda x, y: x & y, "OR": lambda x, y: x | y, "XOR": lambda x, y: x ^ y}

def get_init_values():
    values = {}
    for value in init_values:
        k, v = value.split(": ")
        values[k] = int(v)
    return values

def get_edges_and_operations():
    edges = defaultdict(list)
    operations = {}

    for idx, equation in enumerate(equations):
        operation, result = equation.split(" -> ")
        a, operator, b = operation.split()

        edges[a].append(result)
        edges[b].append(result)
        operations[result] = (a, b, operators_map[operator])
    
    return edges, operations

def fill_values(values, edges, operations):
    todo = list(values.keys())

    while todo:
        v = todo.pop(0)
        finished = True
        for e in edges[v]:
            a, b, f = operations[e]
            if a in values and b in values and f(values[a], values[b]) not in values:
                values[e] = f(values[a], values[b])
                todo.append(e)
            else:
                finished = False
        if not finished: todo.append(v)

def get_z(values):
    z = 0
    for k, v in sorted(values.items(), reverse=True):
        if k.startswith("z"):
            z = (z << 1) | v
        else: break
    return z

def index_of(res):
    for i, eq in enumerate(equations):
        if eq.split(" -> ")[1] == res:
            return i 


def swap_equations(x, y):
    i, j = index_of(x), index_of(y)
    operation_i, result_i = equations[i].split(" -> ")
    operation_j, result_j = equations[j].split(" -> ")
    equations[i] = operation_i + " -> " + result_j
    equations[j] = operation_j + " -> " + result_i


def part1():
    values = get_init_values()
    edges, operations = get_edges_and_operations()
    fill_values(values, edges, operations)

    return get_z(values)


def part2():
    # swap_equations("dsd", "spj")
    # swap_equations("z12", "djg")
    # swap_equations("z19", "kbs")
    # swap_equations("z24", "rpj")

    # djg,dsd,kbs,rpj,spj,z12,z19,z24

    swap_equations("z12", "djg")
    swap_equations("z19", "sbg")
    swap_equations("z37", "dsd")
    swap_equations("mcq", "hjm")

    # djg,dsd,hjm,mcq,sbg,z12,z19,z37
    
    values = get_init_values()
    edges, operations = get_edges_and_operations()
    fill_values(values, edges, operations)
    x, y, z = 0, 0, 0

    for k, v in sorted(values.items(), reverse=True):
        if k.startswith("x"):
            x = (x << 1) | v
        if k.startswith("y"):
            y = (y << 1) | v
        if k.startswith("z"):
            z = (z << 1) | v

    if x+y == z:
        return ",".join(sorted(["djg","dsd","hjm","mcq","sbg","z12","z19","z37"]))
    