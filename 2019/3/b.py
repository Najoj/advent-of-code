import math

""" WARNING UGLY BUT WORKS """


def walk(w):
    c = [(0,0)]
    for step in w:
        d = step[0]
        s = int(step[1:])

        for _ in range(0,s):
                x,y = c[-1]
                if d == 'U':
                        c += [(x,y+1)]
                elif d == 'D':
                        c += [(x,y-1)]
                elif d == 'L':
                        c += [(x-1,y)]
                elif d == 'R':
                        c += [(x+1,y)]
                else:
                        print('hurr durr bug!')
    return c

def find(saves, li):
        rl = []
        for e in saves:
            r = 0
            for l in li:
                r+=1
                if l == e:
                    rl += [r]
        return min(rl)


def s(t):
    a,b = t
    return abs(a)+abs(b)

def m(t):
    a,b = t
    return math.sqrt(a*a+b*b)

file = open('test.txt') 
#file = open('input-a.txt') 
apath = file.readline().strip().split(',')
bpath = file.readline().strip().split(',')

awalk = walk(apath)
bwalk = walk(bpath)

print(awalk)
#print(bwalk)

if len(awalk) < len(bwalk):
        short = awalk
        long_ = bwalk
else:
        short = bwalk
        long_ = awalk

inf = float('inf')
save = (inf,inf)
saves = []

for e in short[1:]:
        if e in long_[1:]:
                # idk
                if s(save) > s(e) or m(save) > m(e):
                        saves += [e]

print(saves)
asteps = find(saves, awalk[1:])
bsteps = find(saves, bwalk[1:])

print(asteps)
print(bsteps)

print(asteps+bsteps)
