import sys
import math

light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

while True:
    remaining_turns = int(input())
    print("TY = ", initial_ty, file=sys.stderr)
    print("TX = ", initial_tx, file=sys.stderr)
    if light_y > initial_ty and light_x > initial_tx:
        print("SE")
        initial_ty += 1
        initial_tx += 1
    elif light_y > initial_ty and light_x < initial_tx:
        print("SW")
        initial_ty += 1
        initial_tx -= 1
    elif light_y < initial_ty and light_x > initial_tx:
        print("NE")
        initial_ty -= 1
        initial_tx += 1
    elif light_y < initial_ty and light_x < initial_tx:
        print("NW")
        initial_ty -= 1
        initial_tx -= 1
    elif light_y > initial_ty:
        print("S")
        initial_ty += 1
    elif light_y < initial_ty:
        print("N")
        initial_ty += 1
    elif light_x > initial_tx:
        print("E")
        initial_tx += 1
    elif light_x < initial_tx:
        print("W")
        initial_tx -= 1
