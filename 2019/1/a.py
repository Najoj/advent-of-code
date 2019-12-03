import math

def calc(i):
        return math.floor(i/3) - 2
sum = 0
with open('input-a.txt') as file:
        for line in file:
            print(sum)
            sum += calc(int(line))

print('svar',sum)
