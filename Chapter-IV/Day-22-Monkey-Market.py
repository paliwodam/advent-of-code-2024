from collections import defaultdict
input_file = "Inputs/Chapter-IV/Day-22-Input.txt"
n = 2000

with open(input_file) as file:
    buyers = [int(line.rstrip()) for line in file]

sequences = defaultdict(int)

def calculate_mix_prune(secret, function):
    x = function(secret)
    secret = x ^ secret
    return secret % 16777216

for b in range(len(buyers)):
    used_sequences = set()
    diff = []
    for i in range(n):
        prev, secret = buyers[b], buyers[b]
        secret = calculate_mix_prune(secret, lambda x: x * 64)
        secret = calculate_mix_prune(secret, lambda x: x // 32)
        secret = calculate_mix_prune(secret, lambda x: x * 2048)
        buyers[b] = secret

        diff.append(secret % 10 - prev % 10)
        if len(diff) > 4: diff.pop(0)
        if tuple(diff) not in used_sequences: sequences[tuple(diff)] += secret % 10
        used_sequences |= {tuple(diff)}

def part1():
    return sum(buyers)

def part2():
    return max(sequences.values())
