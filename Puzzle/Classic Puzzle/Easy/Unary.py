import sys
import re

message = input()
print('message', message, file=sys.stderr)
split = re.compile('1+|0+')
ascii2binary = ''.join(format(ord(i), 'b').zfill(7) for i in message)
myList = split.findall(ascii2binary)
result = ''

for i in myList:
    if i[0] == '1':
        result += '0' + ' ' + len(i) * '0' + ' '
    else:
        result += '00' + ' ' + len(i) * '0' + ' '

print(result.rstrip())
