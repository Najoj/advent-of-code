import math
import re

input_file = 'testdata.txt'


# input_file = 'data.txt'
# input_file = 'my_testdata.txt'


class Cave:
    def __init__(self, _max_x, _min_x, _max_y, _min_y):
        self._max_x = _max_x
        self._min_x = _min_x
        self._max_y = _max_y
        self._min_y = _min_y

        self.width = _max_x - _min_x + 1
        self.height = _max_y - _min_y + 1

        # list of (x,y) tuples
        self.beacons = []
        self.sensors = []

        self.map = [['.'] * self.width] * self.height

    def add(self, sensor, beacon):
        sensor0 = sensor[0] % self.width
        sensor1 = sensor[1] % self.height
        beacon0 = beacon[0] % self.width
        beacon1 = beacon[1] % self.height

        self.sensors.append((sensor0, sensor1))
        self.beacons.append((beacon0, beacon1))

    def __str__(self):
        s = ''
        for row in range(self.width):
            for col in range(self.height):
                c = self.map[row][col]
                if (row, col) in self.sensors:
                    c = 'S'
                if (row, col) in self.beacons:
                    c = 'B'
                s += c
            s += '\n'
        return s


with open(input_file) as f:
    data = f.readlines()

re_line = re.compile(r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)')
max_x = -(2 ** 32)
min_x = +(2 ** 32)
max_y = -(2 ** 32)
min_y = +(2 ** 32)
positions = []
for line in data:
    line = line.strip()
    full_match = re.fullmatch(re_line, line)

    sensor_x = int(full_match[1])
    sensor_y = int(full_match[2])
    beacon_x = int(full_match[3])
    beacon_y = int(full_match[4])

    positions.append(((sensor_x, sensor_y),
                      (beacon_x, beacon_y)))
    #
    if sensor_x > max_x:
        max_x = sensor_x
    if sensor_x < min_x:
        min_x = sensor_x
    if sensor_y > max_y:
        max_y = sensor_y
    if sensor_y < min_y:
        min_y = sensor_y
    #
    if beacon_x > max_x:
        max_x = beacon_x
    if beacon_x < min_x:
        min_x = beacon_x
    if beacon_y > max_y:
        max_y = beacon_y
    if beacon_y < min_y:
        min_y = beacon_y

cave = Cave(max_x, min_x, max_y, min_y)
for position in positions:
    cave.add(position[0], position[1])
    print('---')
    print(cave)
