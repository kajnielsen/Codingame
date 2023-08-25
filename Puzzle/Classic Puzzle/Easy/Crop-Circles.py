import cProfile

alphabet = "abcdefghijklmnopqrstuvwxyz"
size_width, size_height = 19, 25

cornfield = [["{}" for i in range(size_width)] for j in range(size_height)]


def distance(x1, y1, x2, y2, r):
    return (r / 2) > (((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)


def updateField(action, instructions):
    size_width, size_height = len(cornfield[0]), len(cornfield)
    x1, y1, r = (
        alphabet.index(instructions[0]),
        alphabet.index(instructions[1]),
        int(instructions[2:]),
    )
    for i in range(size_height):
        for j in range(size_width):
            if distance(x1, y1, j, i, r):
                if action == "MOW":
                    cornfield[i][j] = "  "
                elif action == "PLANT":
                    cornfield[i][j] = "{}"
                else:
                    if cornfield[i][j] == "{}":
                        cornfield[i][j] = "  "
                    else:
                        cornfield[i][j] = "{}"


def draw():
    size_width, size_height = len(cornfield[0]), len(cornfield)
    for i in range(size_height):
        for j in range(size_width):
            print(cornfield[i][j], end="")
        print()


def main(instructions):
    for i in range(len(instructions)):
        if "PLANTMOW" in instructions[i]:
            updateField("PLANTMOW", instructions[i][len("PLANTMOW") :])
        elif "PLANT" in instructions[i]:
            updateField("PLANT", instructions[i][len("PLANT") :])
        else:
            updateField("MOW", instructions[i])

    draw()


cProfile.run('main(["fg9", "ls11", "oe7"])', sort="ncalls")
