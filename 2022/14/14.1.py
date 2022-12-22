input_file = 'testdata.txt'
input_file = 'data.txt'
# input_file = 'my_testdata.txt'

AIR = '.'
ROCK = '#'
SAND = 'o'
SOURCE = '+'


class Cave:
    def __init__(self, max_x, min_x, max_y, source):
        self._max_x = max_x if max_x > source[0] else source[0]
        self._min_x = min_x
        self._max_y = max_y if max_y > source[1] else source[1]
        self._min_y = 0

        self._source = source

        self._rows = self._max_x - self._min_x + 1
        self._columns = self._max_y - self._min_y + 1

        self._map = [None] * self._columns
        for r in range(self._columns):
            for _ in range(self._rows):
                self._map[r] = [AIR] * self._rows

        sx = source[0] - self._min_x
        sy = source[1]
        self._map[sy][sx] = SOURCE

    def insert(self, line_: list):
        start = line_[0]
        for stop in line_[1:]:
            # same x value, only change in y direction
            if start[1] == stop[1]:
                y = start[1] - self._min_y
                x_start = start[0] - self._min_x
                x_stop = stop[0] - self._min_x

                x_start, x_stop = (x_start, x_stop) if x_start <= x_stop else (x_stop, x_start)
                for x in range(x_start, x_stop + 1):
                    self._map[y][x] = ROCK
            else:
                x = start[0] - self._min_x
                y_start = start[1] - self._min_y
                y_stop = stop[1] - self._min_y

                y_start, y_stop = (y_start, y_stop) if y_start <= y_stop else (y_stop, y_start)
                for y in range(y_start, y_stop + 1):
                    self._map[y][x] = ROCK

            start = stop

    def tick(self, source_=None):
        if source_ is None:
            source_ = self._source
            sx, sy = source_
            sx -= self._min_x

            if self._map[sy][sx] == SAND:
                return False
        else:
            sx, sy = source_
            if self._map[sy][sx] != AIR:
                return False

        if self._map[sy + 1][sx] == AIR:
            return self.tick((sx, sy + 1))
        elif (self._map[sy + 1][sx + 1] != AIR and
              self._map[sy + 1][sx - 1] != AIR):
            self._map[sy][sx] = SAND
            return True
        elif self._map[sy + 1][sx - 1] == AIR:
            return self.tick((sx - 1, sy + 1))
        elif self._map[sy + 1][sx + 1] == AIR:
            return self.tick((sx + 1, sy + 1))
        return False

    def __str__(self):
        s = ''
        for line in self._map:
            s += ''.join(line)
            s += '\n'
        return s


with open(input_file) as f:
    data = f.readlines()

source = (500, 0)

structure = []
max_x = max_y = -1
min_x = min_y = 2 ** 32
for line in data:
    line = line.strip()
    part = []
    for xy in line.split(' -> '):
        x, y = xy.split(',')
        x = int(x)
        y = int(y)
        part.append((x, y))
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
        if x < min_x:
            min_x = x
        if y < min_y:
            min_y = y
    structure.append(part)

part2 = True
if part2:
    print('Running part 2')
    # part two assumptions
    new_max_y = max_y + 2
    assumed_min_x = min_x - 200
    assumed_max_x = max_x + 200
    # Add floor
    floor = [(assumed_min_x, new_max_y), (assumed_max_x, new_max_y)]
    # Add walls
    left_wall = [(assumed_min_x, 0), (assumed_min_x, new_max_y)]
    right_wall = [(assumed_max_x, 0), (assumed_max_x, new_max_y)]

    structure.append(floor)
    structure.append(left_wall)
    structure.append(right_wall)

    max_x = assumed_max_x
    min_x = assumed_min_x
    max_y = new_max_y
else:
    print('Running part 1')

cave = Cave(max_x, min_x, max_y, (500, 0))

for line in structure:
    cave.insert(line)

# print(cave)
i = 0
try:
    while cave.tick():
        i += 1
#        print(cave)
except IndexError:
    pass
    #print(cave)

print(i)
