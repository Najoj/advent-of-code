import re

input_file = 'my_input.txt'
# input_file = 'test_input.txt'
with open(input_file, 'r') as f:
    data = f.readlines()
RED = 'red'
GREEN = 'green'
BLUE = 'blue'
goal = {RED: 12,
        GREEN: 13,
        BLUE: 14}
save_id = []
to_sum = []
for line in data:
    game = {RED: 0, GREEN: 0, BLUE: 0}
    g = line.split(':')[0]
    id = int(re.findall(r'\d+', g)[0])

    ss = line.split(':')[1].split(';')

    for sn in ss:
        for s in sn.split(','):
            for c in game.keys():
                if c in s:
                    num = re.findall(r'\d+', s)[0]
                    game[c] = max(game[c],
                                  int(num))
    # part 1
    possible = True
    for c in game.keys():
        if goal[c] < game[c]:
            possible = False

    if possible:
        save_id.append(id)

    # part 2
    c = game[RED] * game[BLUE] * game[GREEN]
    to_sum.append(c)

id_sum = sum(save_id)
print('Part 1:', id_sum)
cube_sum = sum(to_sum)
print('Part 2:', cube_sum)