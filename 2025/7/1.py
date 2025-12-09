INPUT = 'example.in'
INPUT = 'my.in'

with open(INPUT) as file:
    lines = file.readlines()

def pp(m):
    print(m, end='')

SPLITTER = '^'
SHIP = 'S'

beams = []
hit = 0
for line in lines:
    line = line.strip()
    pp(str(hit))
    for p, c in enumerate(line):
        if beams:
            if p in beams:
                if c == SPLITTER:
                    hit += 1
                    beams.remove(p)
                    if p-1 not in beams: beams.append(p - 1)
                    if p+1 not in beams: beams.append(p + 1)  # nb! skews the print a bit
                    pp(c)
                else:
                    pp('|')
                
            else:
                pp(c)
        elif c == SHIP:
            beams.append(p)
            print(line)
    pp('\n')

print(hit)