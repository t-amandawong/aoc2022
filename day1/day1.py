# aoc day 1 2022!!! so excited :DDDD

max_cals = 0        # most amount of calories
second_cals = 0     # second most amount of calories
third_cals = 0      # third most amount of calories
curr_cals = 0
with open('puzzle_input.txt', 'r') as in_file:
    for line in in_file:
        if line.strip():
            line_calories = int(line.strip())
            curr_cals += line_calories
        else:
            if curr_cals > max_cals:
                third_cals = second_cals    # added for part 2
                second_cals = max_cals      # added for part 2
                max_cals = curr_cals
            elif curr_cals > second_cals:   # added for part 2
                third_cals = second_cals    # added for part 2
                second_cals = curr_cals     # added for part 2
            elif curr_cals > third_cals:    # added for part 2
                third_cals = curr_cals      # added for part 2
            curr_cals = 0

print("most cals: " + str(max_cals))
print("second most cals: " + str(second_cals))
print("third most cals: " + str(third_cals))

print("top 3 total cals: " + str(max_cals + second_cals + third_cals))
