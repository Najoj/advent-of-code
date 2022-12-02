input_file = 'data.txt'
# input_file = 'testdata.txt'
with open(input_file, 'r') as f:
    data = f.readlines()

mapA = {'A': 1,
        'B': 2,
        'C': 3}
mapX = {'X': 1,
        'Y': 2,
        'Z': 3}

point_sum = 0


def compareAX(A, X):
    """
    >>> compareAX(1, 1)
    3
    >>> compareAX(2, 1)
    0
    >>> compareAX(3, 1)
    6
    >>> compareAX(1, 2)
    6
    >>> compareAX(2, 2)
    3
    >>> compareAX(3, 2)
    0
    >>> compareAX(1, 3)
    0
    >>> compareAX(2, 3)
    6
    >>> compareAX(3, 3)
    3
    """
    win= {1: 2,
          2: 3,
          3: 1}
    # draw
    if A == X:
        return 3
    if win[A] == X:
        return 6
    return 0


for line in data:
    A, X = line.strip().split(' ', maxsplit=1)
    A = mapA[A]
    X = mapX[X]
    turn_sum = X + compareAX(A, X)
    point_sum += turn_sum

print(point_sum)
