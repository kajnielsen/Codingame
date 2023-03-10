# https://www.codingame.com/ide/puzzle/retro-typewriter-art

abr = {
    "sp": " ",
    "bS": "\\",
    "sQ": "'",
    "nl": "\n"
}
t = ['1sp', '1/', '1bS', '1_', '1/', '1bS', 'nl', '1(', '1sp', '1o', '1.', '1o', '1sp', '1)', 'nl', '1sp', '1>', '1sp', '1^', '1sp', '1<', 'nl', '2sp', '3|']

print("-----------------------------")
for i in t:
    if i.isdigit():
        j, k = i[:-1], i[-1]
        print(int(j) * k, end='')
    count = 0
    if not i[0].isdigit():
        if i in abr:
            print(abr[i], end='')
            continue
        else:
            print(i, end='')
    for le in range(len(i)):
        if not i[le].isdigit():
            break
        else:
            count += 1

    m, n = i[:count], i[count:]
    if n in abr:
        print(int(m) * abr[n], end='')
    else:
        print(int(m) * n, end='')
