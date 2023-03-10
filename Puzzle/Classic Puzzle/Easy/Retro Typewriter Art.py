# https://www.codingame.com/ide/puzzle/retro-typewriter-art

abr = {
    "sp": " ",
    "bS": "\\",
    "sQ": "'",
    "nl": "\n"
}
t = ['1sp', '1/', '1bS', '1_', '1/', '1bS', 'nl', '1(', '1sp', '1o', '1.', '1o', '1sp', '1)', 'nl', '1sp', '1>', '1sp', '1^', '1sp', '1<', 'nl', '2sp', '3|']


for i in t:
    # print(i)
    if i in abr:
        print(abr[i])
    if i.isdigit():
        j, k = i[:-1], i[-1]
        print(int(j) * k)
    count = 0
    for le in range(len(i)):
        
        if i[le].isdigit():
            count += 1

    m, n = i[:count], i[count:]
    if n in abr:
        print(int(m) * abr[n])
    else:
        print(int(n) * m)   
