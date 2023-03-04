#
# Link: https://www.codingame.com/ide/puzzle/defibrillators
#

import sys
import math

l = []
myDict = {}
lon = float(input().replace(',', '.'))
lat = float(input().replace(',', '.'))

n = int(input())

for i in range(n):
    defib = input().replace(',', '.')
    l.append(defib.split(';'))

for i in l:
    x = (float(i[4]) - lon) * (math.cos((lat + float(i[5])) / 2))
    y = (float(i[5]) - lat)
    d = (math.sqrt(x**2 + y**2)) * 6371
    myDict[d] = i

t = min(myDict)
print(myDict[t][1])
