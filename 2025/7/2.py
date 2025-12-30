#INPUT = 'example.in'
INPUT = 'my.in'
#INPUT = 'test.in'

with open(INPUT) as file:
    lines = file.readlines()

def pp(m):
    print(m, end='')


SPLITTER = '^'
SHIP = 'S'
EMPTY = '.'

paths = 0
line_no = 0
root = None
beams = {}
for n in range(len(lines[0].strip())):
    beams[n] = 0

paths = 0
for line in lines:
    line = line.strip()
    if SPLITTER in line or  SHIP in line:
        for column, c in enumerate(line):
            if c == EMPTY:
                continue
            elif c == SHIP:
                beams[column] = 1
            elif c == SPLITTER:
                beams[column - 1] += beams[column]
                beams[column + 1] += beams[column]
                beams[column] = 0

        paths = 0
        for beam in sorted(beams):
            if beams[beam] > 0:
                print(beam, beams[beam])
                paths += beams[beam]
        print('-'*10)
        
print(paths)
if 'example.in' in INPUT:
    assert paths == 40, f'Got {paths} != 40'