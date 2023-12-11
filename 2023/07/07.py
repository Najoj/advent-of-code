import re

input_file = 'my_input.txt'
#input_file = 'test_input.txt'
with open(input_file, 'r') as f:
    data = f.readlines()


class Hand:
    _card_order = {'A': 12, 'K': 11, 'Q': 10,
                   'J': 9,
                   'T': 8, '9': 7,
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

    def __init__(self, _line: str, part2=False):
        self.part2 = part2
        if part2:
            self._card_order['J'] = -200

        self.hand = _line.split(' ')[0]
        self.bid = int(_line.split(' ')[1])
        self.rank = None
        self.type = self.get_type2() if part2 else self.get_type()

    def __gt__(self, other):
        if other.type != self.type:
            return other.type < self.type
        for oh, sh in zip(other.hand, self.hand):
            if oh != sh:
                return self._card_order[oh] < self._card_order[sh]

    def get_type2(self):
        if 'J' not in self.hand:
            return self.get_type()
        if self.hand == 'JJJJJ':
            return self.FIVE_OF_A_KIND

        max_type = self.HIGH_CARD
        for l in set(self.hand):
            if l != 'J':
                test_hand = self.hand.replace('J', l)
                t = self.get_type(test_hand)
                if max_type < t:
                    max_type = t

        return max_type

    def get_type(self, _hand=None):
        if _hand is None:
            _hand = self.hand

        ls = len(set(_hand))
        if ls == 1:
            # XXXXX
            return self.FIVE_OF_A_KIND

        if ls == 2:
            # XXXXY
            if (_hand.count(_hand[0]) == 1
                    or _hand.count(_hand[0]) == 4):
                return self.FOUR_OF_A_KIND
            # XXXYY
            return self.FULL_HOUSE

        if ls == 3:
            # XXXYZ:
            if re.match(r'^.*(.).*\1.*\1.*$', _hand):
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

print('Part 1:', answer)

hand_bids = []
for line in data:
    hand_bids.append(Hand(line, True))

hand_bids = sorted(hand_bids)
rank = 0
answer = 0
for hb in hand_bids:
    rank += 1
    answer += rank * hb.bid

print('Part 2:', answer)
