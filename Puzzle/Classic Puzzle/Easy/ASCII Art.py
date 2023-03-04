import sys

l = int(input())
h = int(input())
t = input()
t = t.upper()

list1 = []
myDict = {}
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ?"

for i in range(len(t)):
    if t[i] not in alphabet:
        t = t.replace(t[i], '?')        

for i in alphabet:
    myDict[i] = []

for i in range(h):
    row = input()
    chunks = [row[i:i+l] for i in range(0, len(row), l)]
    for j in range(len(alphabet)):
        x = myDict.get(alphabet[j])
        x.append(chunks[j])
        myDict[alphabet[j]] = x
      
for loop in range(h):    
    print_string = ""
    for letter in t:
        if letter in myDict:            
            x = myDict.get(letter)
            print_string += x[loop]
    print(print_string)
