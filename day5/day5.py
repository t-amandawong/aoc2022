# aoc day5
import numpy as np

# compile all crates in nested lists
crates = []
with open('crates.txt', 'r') as file:
    for line in file:
        line = line.rstrip()
        while len(line) < 36:
            line += " "
        curr_crates = [line[i] for i in range(1, len(line), 4)]
        crates.append(curr_crates)

# transpose crates, reverse order of each row, and delete whitespace elements
transposed_crates = np.array(crates).T.tolist()
for row in transposed_crates:
    row.reverse()
    for i in range(len(row)):
        if row[i] == " ":
            del row[i:]
            break

# open file with instructions
with open('orders.txt', 'r') as file2:
    for line in file2:
        line = line.rstrip().split()
        amount, start, end = [int(i) for i in line if i.isdigit()]
        # take care of off by 1 errors with list indexing
        start -= 1
        end -= 1
        crates_to_move = transposed_crates[start][-amount:]
        del transposed_crates[start][-amount:]
        # next line needed for part 1, commented out for part 2
        # crates_to_move.reverse()
        transposed_crates[end].extend(crates_to_move)

for crates in transposed_crates:
    print(crates[-1], end='')
