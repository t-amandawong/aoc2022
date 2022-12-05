# day 2 aoc 2022!!

# rock: A = X
# paper: B = Y
# scissors: C = Z

# rock: A = X, paper: B = Y, scissors: C = Z
# A beats Z, B beats X, C beats Y
# X beats C, Y beats A, Z beats B
# X = 1, Y = 2, Z = 3
# 0 for loss, 3 for draw, 6 for win

total_score = 0
with open('input.txt', 'r') as file:
    for line in file:
        line_split = line.split()
        opp_play = line_split[0]
        my_play = line_split[1]
        if opp_play == 'A':
            if my_play == 'X':  # draw
                score = 3 + 1
            elif my_play == 'Y':    # win
                score = 6 + 2
            else:   # my_play == 'Z', loss
                score = 0 + 3
        elif opp_play == 'B':
            if my_play == 'X':  # loss
                score = 0 + 1
            elif my_play == 'Y':  # draw
                score = 3 + 2
            else:  # my_play == 'Z', win
                score = 6 + 3
        else:   # opp_play == 'C'
            if my_play == 'X':  # win
                score = 6 + 1
            elif my_play == 'Y':    # loss
                score = 0 + 2
            else:   # my_play == 'Z', draw
                score = 3 + 3
        total_score += score

print(total_score)

# pt 2 code
# rock: A = 1
# paper: B = 2
# scissors: C = 3

# rock: A = 1, paper: B = 2, scissors: C = 3
# A beats C, B beats A, C beats B
# X = loss, Y = draw, Z = win
# 0 for loss, 3 for draw, 6 for win

total_score2 = 0
with open('input.txt', 'r') as file2:
    for line in file2:
        line_split = line.split()
        opp_play = line_split[0]
        outcome = line_split[1]
        if outcome == 'X':  # loss = 0
            if opp_play == 'A':     # my play is C
                score = 0 + 3
            elif opp_play == 'B':     # my play is A
                score = 0 + 1
            else:   # opp_play == 'C', my play is B
                score = 0 + 2
        elif outcome == 'Y':    # draw = 3
            if opp_play == 'A':     # my play is A
                score = 3 + 1
            elif opp_play == 'B':   # my play is B
                score = 3 + 2
            else:   # opp_play == 'C', my play is C
                score = 3 + 3
        else:   # outcome == 'Z', win = 6
            if opp_play == 'A':     # my play is B
                score = 6 + 2
            elif opp_play == 'B':   # my play is C
                score = 6 + 3
            else:   # opp_play == 'C, my play is A
                score = 6 + 1
        total_score2 += score

print(total_score2)
