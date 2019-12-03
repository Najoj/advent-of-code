import math

def calc(i):
        return math.floor(i/3) - 2

def round(k):
    sum = 0
    while k > 0:
        k = calc(k)
        sum += k
    sum -= k
    return sum

with open('input-b.txt') as file:
        sum = 0
        for line in file:
                sum += round(int(line))

print('svar',sum)
