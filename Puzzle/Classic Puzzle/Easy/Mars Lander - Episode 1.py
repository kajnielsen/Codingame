surface_n = int(input())
for i in range(surface_n):
    land_x, land_y = [int(j) for j in input().split()]

# game loop
count  = 10
while True:
    count += 1
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]
    if v_speed < -40 and count > 20:
        if power <= 3:
            power += 1
    elif v_speed >= -39:
        if power >= 1:
            power -= 1
    print("0 " + str(power))
