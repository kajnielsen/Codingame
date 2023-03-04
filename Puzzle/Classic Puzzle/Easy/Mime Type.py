import sys
import math

db = {}

n = int(input())
q = int(input())

for i in range(n):
    ext, mt = input().split()
    db[ext.lower()] = mt


for i in range(q):
    fname = input().lower()
    target = "."
    x = fname.rfind(target)
    test = fname[x + 1:]
    if test in db and x > -1:
        print(db[fname[x + 1:]])
    else:
        print("UNKNOWN")
