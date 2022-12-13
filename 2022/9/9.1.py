test_file = 'testdata.txt'
my_test_file = 'mytest.txt'
input_file = my_test_file
input_file = test_file
input_file = 'data.txt'

with open(input_file) as f:
    data = f.readlines()


class Grid:
    def __init__(self):
        # (x, y)
        self.head_position = (0, 0)
        self.tail_position = (0, 0)
        self.tail_visited = [(0, 0)]

    def walk(self, direction, steps):
        if steps >= 1:
            for _ in range(steps):
                self._walk_one(direction)
                # print(self)
        elif steps != 0:
            raise ValueError('Unhandled step size:', steps)

    def _walk_one(self, direction):
        hx, hy = self.head_position
        tx, ty = self.tail_position

        if 'U' == direction:
            hy += 1
            diffx, diffy = hx - tx, hy - ty
            if diffx == 0:
                if diffy > 1:
                    ty += 1
            elif diffx > 0:
                if diffy > 1:
                    tx += 1
                    ty += 1
                elif diffy < -1:
                    tx += 1
                    ty += -1
            elif diffx < 0:
                if diffy > 1:
                    tx += -1
                    ty += 1
                elif diffy < -1:
                    tx += -1
                    ty += -1

        elif 'D' == direction:
            hy += -1
            diffx, diffy = hx - tx, hy - ty
            if diffx == 0:
                if diffy < -1:
                    ty += -1
            elif diffx > 0:
                if diffy > 1:
                    tx += 1
                    ty += 1
                elif diffy < -1:
                    tx += 1
                    ty += -1
            elif diffx < 0:
                if diffy > 1:
                    tx += -1
                    ty += -1
                elif diffy < -1:
                    tx += -1
                    ty += -1

        elif 'R' == direction:
            hx += 1
            diffx, diffy = hx - tx, hy - ty
            if diffy == 0:
                if diffx > 1:
                    tx += 1
            elif diffy > 0:
                if diffx > 1:
                    tx += 1
                    ty += 1
                elif diffx < -1:
                    tx += -1
                    ty += 1
            elif diffy < 0:
                if diffx > 1:
                    tx += 1
                    ty += -1
                elif diffx < -1:
                    tx += -1
                    ty += -1

        elif 'L' == direction:
            hx += -1
            diffx, diffy = hx - tx, hy - ty
            if diffy == 0:
                if diffx < -1:
                    tx += -1
            elif diffy > 0:
                if diffx > 1:
                    tx += 1
                    ty += 1
                elif diffx < -1:
                    tx += -1
                    ty += 1
            elif diffy < 0:
                if diffx > 1:
                    tx += 1
                    ty += -1
                elif diffx < -1:
                    tx += -1
                    ty += -1

        else:
            raise ValueError('Direction:' + direction)

        self.head_position = (hx, hy)
        self.tail_position = (tx, ty)
        if self.tail_position not in self.tail_visited:
            self.tail_visited.append(self.tail_position)

    def __str__(self) -> str:
        xmax = max(x for (x, _) in self.tail_visited)
        xmin = min(x for (x, _) in self.tail_visited)
        ymax = max(y for (_, y) in self.tail_visited)
        ymin = min(y for (_, y) in self.tail_visited)

        s = ''
        for y in reversed(range(ymin - 2, ymax + 2)):
            for x in range(xmin - 2, xmax + 2):
                xy = (x, y)
                if xy == self.head_position:
                    s += 'h' if xy in self.tail_visited else 'H'
                elif xy == self.tail_position:
                    s += 't' if xy in self.tail_visited else 'T'
                elif xy in self.tail_visited:
                    s += '#'
                elif xy == (0, 0):
                    s += 's'
                else:
                    s += '.'
            s += '\n'

        return s


grid = Grid()
for line in data:
    line = line.strip()
    direction_, steps_ = line.split(' ', maxsplit=1)
    steps_ = int(steps_)
    grid.walk(direction_, steps_)

print(grid)

tail_visited = len(grid.tail_visited)
assert 13 == tail_visited if test_file == input_file else True
print(tail_visited)
