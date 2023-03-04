import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
t = []
n = int(input())  # the number of temperatures to analyse
for i in input().split():
    t.append(int(i))
if len(t) > 0:
    t.sort(reverse=True)
    print(min(t, key=lambda x:abs(x-0)))
else:
    print(0)
