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

def s(t):
    a,b = t
    return a+b

def m(t):
    a,b = t
    return math.sqrt(a*a+b*b)

file = open('test.txt') 
file = open('input-a.txt') 
apath = file.readline().strip().split(',')
bpath = file.readline().strip().split(',')

awalk = walk(apath)
bwalk = walk(bpath)

#print(awalk)
#print(bwalk)

if len(awalk) < len(bwalk):
        short = awalk
        long_ = bwalk
else:
        short = bwalk
        long_ = awalk

inf = float('inf')
save = inf,inf

for e in short[1:]:
        if e in long_[1:]:
                # idk
                if s(save) > s(e) or m(save) > m(e):
                        save = e
                        #print(save)
#print(save)
print(m(save))

