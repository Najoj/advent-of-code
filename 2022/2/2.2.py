input_file = 'data.txt'
# input_file = 'testdata.txt'
with open(input_file, 'r') as f:
    data = f.readlines()

ROCK = 1
PAPER = 2
SCISSORS = 3
mapA = {'A': ROCK,
        'B': PAPER,
        'C': SCISSORS}
mapX = {'X': ROCK,
        'Y': PAPER,
        'Z': SCISSORS}

point_sum = 0


def compareAX(A, X):
    """
    >>> compareAX(1, 1)
    3
    >>> compareAX(2, 1)
    1
    >>> compareAX(3, 1)
    2
    >>> compareAX(1, 2)
    4
    >>> compareAX(2, 2)
    5
    >>> compareAX(3, 2)
    6
    >>> compareAX(1, 3)
    8
    >>> compareAX(2, 3)
    9
    >>> compareAX(3, 3)
    7
    """
    win = {ROCK: PAPER,
           PAPER: SCISSORS,
           SCISSORS: ROCK}
    draw = {ROCK: ROCK,
            PAPER: PAPER,
            SCISSORS: SCISSORS}
    loose = {ROCK: SCISSORS,
             PAPER: ROCK,
             SCISSORS: PAPER}
    if X == 1:
        return loose[A] + 0
    if X == 2:
        return draw[A] + 3
    if X == 3:
        return win[A] + 6


for line in data:
    A, X = line.strip().split(' ', maxsplit=ROCK)
    A = mapA[A]
    X = mapX[X]
    turn_sum = compareAX(A, X)
    point_sum += turn_sum

print(point_sum)
