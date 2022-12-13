test_file = 'testdata2.txt'
my_test_file = 'mytest.txt'
my_data_file = 'data.txt'

input_file = test_file
# input_file = my_test_file
input_file = my_data_file

with open(input_file) as f:
    data = f.readlines()

XPOS = 0
YPOS = 1


class Knot:
    def __init__(self, knot_name: int):
        self.knot_name = knot_name
        self.knot_position = (0, 0)
        self.knot_visits = [(0, 0)]

        if knot_name == 9:
            self.next_knot = None
        else:
            self.next_knot = Knot(knot_name + 1)

    def walk_one(self, direction):
        if 'U' == direction:
            self.move_up()
        elif 'D' == direction:
            self.move_down()
        elif 'R' == direction:
            self.move_right()
        elif 'L' == direction:
            self.move_left()
        else:
            raise ValueError('Direction:' + str(direction))

        self._mark_visited()

    def _mark_visited(self):
        if self.knot_position != self.knot_visits[-1]:
            self.knot_visits.append(self.knot_position)
        if self.next_knot is not None:
            self.next_knot._mark_visited()

    def _move_next(self):
        hx, hy = self.knot_position
        tx, ty = self.next_knot.knot_position
        diffx, diffy = hx - tx, hy - ty

        if abs(diffx) >= 2 or abs(diffy) >= 2:
            if hx > tx:
                self.next_knot.move_right(hy != ty)
            elif hx < tx:
                self.next_knot.move_left(hy != ty)
            if hy > ty:
                self.next_knot.move_up()
            elif hy < ty:
                self.next_knot.move_down()

    def move_up(self, ignore_next=False):
        hx, hy = self.knot_position
        hy += 1
        self.knot_position = (hx, hy)
        if not ignore_next and self.next_knot is not None:
            self._move_next()
        return self

    def move_down(self, ignore_next=False):
        hx, hy = self.knot_position
        hy -= 1
        self.knot_position = (hx, hy)
        if not ignore_next and self.next_knot is not None:
            self._move_next()

        return self

    def move_right(self, ignore_next=False):
        hx, hy = self.knot_position
        hx += 1
        self.knot_position = (hx, hy)
        if not ignore_next and self.next_knot is not None:
            self._move_next()
        return self

    def move_left(self, ignore_next=False):
        hx, hy = self.knot_position
        hx -= 1
        self.knot_position = (hx, hy)
        if not ignore_next and self.next_knot is not None:
            self._move_next()
        return self

    def __eq__(self, other):
        if isinstance(other, Knot):
            return self.knot_position == other.knot_position
        if (isinstance(other, tuple) and
                len(other) == 2 and
                isinstance(other[XPOS], int) and
                isinstance(other[YPOS], int)):
            return self.knot_position == other
        return False

    def __str__(self):
        return self.knot_name

    def __getitem__(self, item):
        if isinstance(item, int):
            if item == self.knot_name:
                return self
            return self.next_knot[item]
        raise IndexError(f'No item {item}')

    def who_visited(self, x, y):
        if (x, y) == self.knot_position:
            return True, self.knot_name

        elif self.next_knot is not None:
            b, n = self.next_knot.who_visited(x, y)
            if b:
                return b, n

        if (x, y) in self.knot_visits:
            return True, self.knot_name

        else:
            return False, None


def print_knots(head_knot: Knot) -> str:
    xmax = max(x for (x, _) in head_knot.knot_visits)
    xmin = min(x for (x, _) in head_knot.knot_visits)
    ymax = max(y for (_, y) in head_knot.knot_visits)
    ymin = min(y for (_, y) in head_knot.knot_visits)

    nine_visits = head_knot[9].knot_visits
    s = ''
    for y in reversed(range(ymin - 2, ymax + 2)):
        for x in range(xmin - 2, xmax + 2):
            any_visited, visited = head_knot.who_visited(x, y)
            if (x, y) in nine_visits:
                s += '#'
            elif any_visited:
                if visited is not None and visited == 9:
                    s += str(visited)
                else:
                    s += '.'
                # else:
                #    print('#', end='')
            elif x == 0 and y == 0:
                s += 's'
            else:
                s += '.'
        s += '\n'
    return s


head_knot = Knot(0)
for line in data:
    line = line.strip()
    direction_, steps_ = line.split(' ', maxsplit=1)
    steps_ = int(steps_)

    if steps_ >= 1:
        for _ in range(steps_):
            head_knot.walk_one(direction_)

    elif steps_ != 0:
        raise ValueError('Unhandled step size:', steps_)


print(print_knots(head_knot))
tail_visited = len(set(head_knot[9].knot_visits))

assert 36 == tail_visited if test_file == input_file else True
assert tail_visited < 2911
