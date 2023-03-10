import sys
import math

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
rotors = []  #  Addind the alphabet as rotor number 0

operation = input()  #  Encode or decode
prn = int(input())  #  Starting shift


for i in range(3):
    rotor = input()  #  Value of each rotor as it inputs
    rotors.append(rotor)

message = input()  #  message to encode or decode

def enigma_encode(rotors, prn, message):
    encoded_message = shift(message, prn, 'ENCODE')
    for j in rotors:
        encoded_message = substitute(j, encoded_message, 'ENCODE')
    return encoded_message

def enigma_decode(rotors, prn, message):    
    decoded_message = message
    rotors.reverse()
    for k in rotors:
        decoded_message = substitute(k, decoded_message, 'DECODE')
    decoded_message = shift(decoded_message, prn, 'DECODE')
    return decoded_message
    
    

def shift(message, prn, operation):
    result = ""
    for i in range(len(message)):
        t = alpha.index(message[i])
        if operation == 'ENCODE':
            target = (t + prn + i)
            while (target) >= len(alpha) -1:
                target -= len(alpha)
            result += alpha[target]
        
        elif operation == 'DECODE':
            target = (t - prn - i)
            while (target) < 0:
                target += len(alpha)
            result += alpha[target]
        
    return result

def substitute(rotor, message, operation):
    result = ""
    if operation == 'ENCODE':
        for i in range(len(message)):
            result += rotor[alpha.index(message[i])]
    if operation == 'DECODE':
        for i in range(len(message)):
            result += alpha[rotor.index(message[i])]
        pass
    return result


if operation == 'ENCODE':
    print(enigma_encode(rotors, prn, message))
elif operation == 'DECODE':
    print(enigma_decode(rotors, prn, message))
