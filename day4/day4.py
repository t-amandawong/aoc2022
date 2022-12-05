
lines = []
count = 0
with open('input.txt', 'r') as file:
    for line in file:
        sections = line.rstrip().split(',')
        start1, end1 = [int(x) for x in sections[0].split('-')]
        start2, end2 = [int(x) for x in sections[1].split('-')]
        # part 1 code
        # if start1 <= start2 and end1 >= end2:
        #     count += 1
        # elif start2 <= start1 and end2 >= end1:
        #     count += 1
        # else:
        #     continue
        for i in range(start1, end1 + 1):
            if i in range(start2, end2 + 1):
                count += 1
                break

print(count)
