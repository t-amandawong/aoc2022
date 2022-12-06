
with open('input.txt', 'r') as file:
    line = file.readline().rstrip()

# marker length is 4 for part 1, 14 for part 2
marker_length = 14
for i in range(len(line)):
    possible_marker = line[i:i+marker_length]
    if len(possible_marker) == len(set(possible_marker)):
        marker = possible_marker
        num_chars = i + marker_length
        break

print(num_chars)
