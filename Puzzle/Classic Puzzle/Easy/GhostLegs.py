import sys
import math

GL = [['A  B  C'],
      ['|  |  |'],
      ['|--|  |'],
      ['|  |--|'],
      ['|  |--|'],
      ['|  |  |'],
      ['1  2  3']]

w, h = 7, 7

for i in range(0, w, 3):
    start_point = GL[0][0][i]
    endpoint = ""
    AL = i

    for j in range(h):
        for k in range(1, w, 3):
            if GL[j][0][k] == '-':
                print(abs(k))
                if k > AL and (k - AL) < 3:
                    AL += 3
                elif k < AL and (AL - k < 3):
                    AL -= 3
    print(f"{start_point}{GL[h-1][0][AL]}")
        