import sys

lst = []

def test(nums):
    s = sorted(set(nums))
    return min([[a, b] for a, b in zip(s, s[1:])], key=lambda x: x[1] - x[0])

n = int(input())
for i in range(n):
    pi = int(input())
    lst.append(pi)

rlst = test(lst)
print(rlst[1] - rlst[0])
