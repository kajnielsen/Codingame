import bisect, sys

N = int(input())
horses = []
mini =  sys.maxsize
diff = None

for i in range(N):
    bisect.insort(horses, int(input()))

for i in range(N-1):
    diff = horses[i+1] - horses[i]
    if diff < mini:
        mini = diff

print(mini)
