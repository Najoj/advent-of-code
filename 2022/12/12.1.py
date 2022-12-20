input_file = 'testdata.txt'
input_file = 'data.txt'
#input_file = 'my_testdata.txt'

X = 0
Y = 1

NORTH = 0
EAST = 1
WEST = 2
SOUTH = 3
DIRECTIONS = [NORTH, EAST, SOUTH, WEST]


class MountainChain:
    def __init__(self, rows, columns):
        self._roms = rows
        self._columns = columns
        self.start = None
        self.end = None
        self.map = [None] * rows
        self.visited = set()
        for r in range(rows):
            for _ in range(columns):
                self.map[r] = [None] * columns

    def add(self, x, y, h):
        self.map[y][x] = h

    def start_position(self, x, y):
        self.start = (x, y)
        self.add(x, y, 0)

    def end_position(self, x, y):
        self.end = (x, y)
        self.add(x, y, ord('z') - ord('a') + 1)

    def seek(self) -> int:
        start_x, start_y = self.start
        self.visited.add((start_x, start_y))
        walk = self.find_neighbours(start_x, start_y)
        print(self)
        return self._seek(walk) + 1

    def find_neighbours(self, start_x, start_y):
        walk = []
        neighbours = [(start_x + 0, start_y + 1),
                      (start_x + 1, start_y + 0),
                      (start_x + 0, start_y - 1),
                      (start_x - 1, start_y + 0)]
        for neighbour_x, neighbour_y in neighbours:
            if (0 <= neighbour_x < self._columns and
                    0 <= neighbour_y < self._roms and
                    self.map[neighbour_y][neighbour_x] <= self.map[start_y][start_x] + 1 and
                    (neighbour_x, neighbour_y) not in self.visited):
                walk.append((neighbour_x, neighbour_y))
                self.visited.add((neighbour_x, neighbour_y))
        return walk

    def _seek(self, walk) -> int:
        next_walk = []
        if not walk:
            raise ValueError('Next iteration is empty.')
        if self.end in walk:
            return 0
        for neighbour in walk:

            start_x, start_y = neighbour
            self.visited.add((start_x, start_y))
            neighbours = [(start_x + 0, start_y + 1),
                          (start_x + 1, start_y + 0),
                          (start_x + 0, start_y - 1),
                          (start_x - 1, start_y + 0)]

            for neighbour_x, neighbour_y in neighbours:
                if (0 <= neighbour_x < self._columns and
                        0 <= neighbour_y < self._roms and
                        self.map[neighbour_y][neighbour_x] <= self.map[start_y][start_x] + 1 and
                        (neighbour_x, neighbour_y) not in self.visited):
                    next_walk.append((neighbour_x, neighbour_y))
                    self.visited.add((neighbour_x, neighbour_y))
        print(self)
        return self._seek(next_walk) + 1

    def __str__(self) -> str:
        s = ''
        for r in range(self._roms):
            for c in range(self._columns):
                if (c, r) == self.start:
                    s += '+'
                elif (c, r) == self.end:
                    s += '*'
                elif (c, r) in self.visited:
                    s += '.'
                    # s += chr(self.map[r][c] + ord('A'))
                else:
                    s += chr(self.map[r][c] + ord('a'))

            s += '\n'
        return s


with open(input_file) as f:
    data = f.readlines()

mountains = None

y_ = 0
for line in data:
    line = line.strip()

    if mountains is None:
        mountains = MountainChain(len(data), len(line))

    x_ = 0
    for letter in line:
        h = ord(letter) - ord('a')
        if letter == 'S':
            mountains.start_position(x_, y_)
        elif letter == 'E':
            mountains.end_position(x_, y_)
        else:
            mountains.add(x_, y_, h)

        x_ += 1
    y_ += 1

print(mountains.seek())
