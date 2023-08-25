import sys

li = []
n = int(input())
for i in range(n):
    line = input()
    li += [line]


def get_distance(launcher_index, plane_index, plane_height):
    return abs(launcher_index - plane_index) - plane_height - 1


sky_width = len(li[0])
targets = ["WAIT" for h in range(sky_width * (n - 1))]
launcher = li[n - 1].index("^")

for i in range(n):
    for j in range(sky_width):
        if any(item in li[i][j] for item in [">", "<"]):
            targets[get_distance(launcher, j, (n - 1 - i))] = "SHOOT"


shooting_solution = len(targets) - 1 - targets[::-1].index("SHOOT")

for i in range(shooting_solution + 1):
    print(targets[i])
