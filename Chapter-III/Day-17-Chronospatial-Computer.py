from collections import defaultdict
A, B, C = 109020013201563, 0, 0
instruction_pointer = 0
output = []

program = [2,4,1,5,7,5,0,3,4,1,1,6,5,5,3,0]
n = len(program)

def combo(operand):
    if operand == 4: return A
    if operand == 5: return B
    if operand == 6: return C
    return operand

def adv(operand):
    global A
    A = A >> combo(operand)

def bxl(operand):
    global B
    B = B ^ operand

def bst(operand):
    global B
    B = combo(operand) & 7

def jnz(operand):
    global A, instruction_pointer
    if A != 0 and instruction_pointer != operand - 2: 
        instruction_pointer = operand - 2

def bxc(operand):
    global B, C
    B = B ^ C

def out(operand):
    output.append(combo(operand) & 7)

def bdv(operand):
    global A, B
    B = A >> combo(operand)

def cdv(operand):
    global A, C
    C = A >> combo(operand)  

opcodes = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]

def run_program():
    global output, instruction_pointer
    output, instruction_pointer = [], 0
    
    while instruction_pointer < n-1:
        opcode = program[instruction_pointer]
        operand = program[instruction_pointer+1]
        opcodes[opcode](operand)
        instruction_pointer += 2


def find_A(x, idx):
    global A, output
    if idx < 0:
        return x
    for i in range(8):
        A = x*8 + i
        run_program()
        if output and output[0] == program[idx]:
            print(output)
            result = find_A((x*8+i), idx-1)
            if result != 0: return result
    return 0


def part1():
    global A
    A = 47719761
    run_program()
    return output

def part2():
    return find_A(0, n-1)
