# aoc day 3 :(

az_dict = {}
priority_value = 0

# set priority values for lowercase letters
for i in range(97, 123):
    priority_value += 1
    az_dict[chr(i)] = priority_value

# set priority values for uppercase letters
for i in range(65, 91):
    priority_value += 1
    az_dict[chr(i)] = priority_value

lines = []
total_priority = 0
with open('input.txt', 'r') as file:
    for file_line in file:
        lines.append(file_line.strip())

for line in lines:
    midpoint = int(len(line) / 2)
    str1 = line[:midpoint]
    str2 = line[midpoint:]
    for char in str1:
        if char in str2:
            common_char = char
    priority = az_dict[common_char]
    total_priority += priority

print(total_priority)

# pt 2
grouped_lines = []
for i in range(0, len(lines), 3):
    grouped_lines.append(lines[i: i + 3])

total_priority = 0
for group in grouped_lines:
    for char3 in group[0]:
        if char3 in group[1] and char3 in group[2]:
            common_char = char3
    priority = az_dict[common_char]
    total_priority += priority

print(total_priority)
