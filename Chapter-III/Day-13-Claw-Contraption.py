import re
import numpy as np
from math import inf
input_file = "Inputs/Chapter-III/Day-13-Input.txt"

with open(input_file) as file:
    data = file.read().rstrip()
    configurations = data.split("\n\n")

def part1():
    total = 0
    for conf in configurations:
        conf_A, conf_B, conf_prize = conf.split("\n")
        X_A, Y_A = map(int, re.findall(r'\d+', conf_A))
        X_B, Y_B = map(int, re.findall(r'\d+', conf_B))
        X_prize, Y_prize = map(int, re.findall(r'\d+', conf_prize))
        
        tokens = inf  

        for A in range(100):
            for B in range(100):
                X, Y = A * X_A + B * X_B, A * Y_A + B * Y_B 
                if X == X_prize and Y == Y_prize:
                    tokens = min(tokens, 3 * A + B)
                if X > X_prize or Y > Y_prize:
                    break
        if tokens != inf: total += tokens
    return total


def part2():
    total = 0
    for conf in configurations:
        conf_A, conf_B, conf_prize = conf.split("\n")
        X_A, Y_A = map(int, re.findall(r'\d+', conf_A))
        X_B, Y_B = map(int, re.findall(r'\d+', conf_B))
        X_prize, Y_prize = map(int, re.findall(r'\d+', conf_prize))
        
        M = np.array([[X_A, X_B], [Y_A, Y_B]])
        P = np.array([X_prize, Y_prize]) + 10000000000000
        a,b = map(round, np.linalg.solve(M, P))
        total += a*3+b if [a*X_A+b*X_B,a*Y_A+b*Y_B]==[*P] else 0

    return total