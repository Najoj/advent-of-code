import copy
import math
import re

input_file = 'my_input.txt'
#input_file = 'test_input.txt'
with open(input_file, 'r') as f:
    data = f.readlines()

re_card = re.compile(r'Card (\d+):')
game_points = []
game_cards = []
number_of_cards = [1] * len([n for n in data if n])
for line in data:
    card, numbers = line.split(':')
    winning, mine = numbers.split('|')

    card_no = [int(i) for i in re.findall(r'Card +(\d+)', card)]
    assert len(card_no) == 1
    card_no = card_no[0]
    winning_no = [int(i) for i in re.findall(r'(\d+)', winning)]
    mine_no = [int(i) for i in re.findall(r'(\d+)', mine)]

    card_points = 0
    for i in winning_no:
        if i in mine_no:
            if card_points == 0:
                card_points = 1
            else:
                card_points *= 2
    game_points.append(card_points)

    if card_points > 0:
        n_cards = int(math.log2(card_points) + 1)
        for n in range(0, n_cards):
            bonus = card_no + n
            number_of_cards[bonus] += number_of_cards[card_no-1]
        #print(number_of_cards)

print('Part 1:', sum(game_points))
number_of_cards = sum(number_of_cards)
print('Part 2:', number_of_cards)
