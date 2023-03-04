mountain_h = {}
while True:
    
    for i in range(8):
        mountain_h[i] = input()
    MaxDictVal = max(mountain_h, key=mountain_h.get)
    print(MaxDictVal)
    del mountain_h[MaxDictVal]
