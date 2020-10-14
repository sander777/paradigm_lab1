import math
import random

def F(x):
    return 2*math.pi*x

def solve(x_m, y_m, x_M, y_M, n):
    sum = 0
    in_field = 0
    for _ in range(n):
        u1 = random.random()
        u2 = random.random()
        x = (x_M - x_m) * u1 + x_m
        y = (y_M - y_m) * u2 + y_m
        f = F(x)
        sum += 1
        if f >= y and y >= 0:
            in_field += 1
        if f <= y and y <= 0:
            in_field -= 1
    dens = float(in_field) / sum
    s = (x_M - x_m) * (y_M - y_m)
    res = dens * s * 4
    return res

r = [1, 2, 3, 4, 5, 6]

for i in r:
    print(solve(0, 0, i, i, 1000000))