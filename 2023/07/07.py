import re

input_file = 'my_input.txt'
# input_file = 'test_input.txt'
with open(input_file, 'r') as f:
    data = f.readlines()


class Hand:
    _card_order = {'A': 12, 'K': 11, 'Q': 10,
                   'J': 9, 'T': 8, '9': 7,
                   '8': 6, '7': 5, '6': 4,
                   '5': 3, '4': 2, '3': 1,
                   '2': 0}
    FIVE_OF_A_KIND = 6
    FOUR_OF_A_KIND = 5
    FULL_HOUSE = 4
    THREE_OF_A_KIND = 3
    TWO_PAIR = 2
    ONE_PAIR = 1
    HIGH_CARD = 0

    def __init__(self, _line: str):
        self.hand = _line.split(' ')[0]
        self.bid = int(_line.split(' ')[1])
        self.rank = None
        self.type = self.get_type()

    def __gt__(self, other):
        if other.type != self.type:
            return other.type < self.type
        for oh, sh in zip(other.hand, self.hand):
            if oh != sh:
                return self._card_order[oh] < self._card_order[sh]

    def get_type(self):
        ls = len(set(self.hand))
        if ls == 1:
            # XXXXX
            return self.FIVE_OF_A_KIND

        if ls == 2:
            # XXXXY
            if (re.match(r'^(.)\1{3}.$', self.hand)
                    or re.match(r'^(.)\1{2}.\1$', self.hand)
                    or re.match(r'^(.)\1.\1{2}$', self.hand)
                    or re.match(r'^(.).\1\1{3}$', self.hand)
                    or re.match(r'^.(.)\1\1{3}$', self.hand)):
                return self.FOUR_OF_A_KIND
            # XXXYY
            return self.FULL_HOUSE

        if ls == 3:
            # XXXYZ:
            if re.match(r'^.*(.).*\1.*\1.*$', self.hand):
                return self.THREE_OF_A_KIND
            return self.TWO_PAIR

        if ls == 4:
            return self.ONE_PAIR
        return self.HIGH_CARD

    def __repr__(self):
        return self.hand


hand_bids = []
for line in data:
    hand_bids.append(Hand(line))

hand_bids = sorted(hand_bids)
rank = 0
answer = 0
for hb in hand_bids:
    rank += 1
    answer += rank * hb.bid

print(answer)
assert answer != 248512134
assert answer != 248367728
assert answer != 248280230
