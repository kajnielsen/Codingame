import sys
import math

width = int(input())
height = int(input())

lines = [["x" for a in range(width)] for b in range(height)]

for c in range(height):
    line = input()
    lines[c] = [*line]

for i in range(len(lines)):
    for j in range(len(lines[0])):
        result = ""
        if lines[i][j] == "0":
            result += f"{j} {i}"
            lines[i][j] = "C"

            if "0" in lines[i]:
                result += f' {lines[i].index("0")} {i}'
            else:
                result += f" -1 -1"
            if i == len(lines) - 1:
                result += f" -1 -1"
            else:
                for k in range(i + 1, len(lines)):
                    if lines[k][j] == "0":
                        result += f" {j} {k}"
                        break
                    elif k == len(lines) - 1:
                        result += f" -1 -1"

        if result == "":
            continue
        print(result)
