import math
import random
import matplotlib.pyplot as plt
import scipy.stats as ss

def a_1():
    return (- math.log(random.uniform(0, 1))) ** 0.5 * math.cos(2 * math.pi * random.uniform(0, 1))

def a_2():
    return (- math.log(random.uniform(0, 1))) ** 0.5 * math.sin(2 * math.pi * random.uniform(0, 1))

def b(n):
    sum = 0
    for _ in range(n):
        sum += random.uniform(0, 1) - 0.5
    return sum * (12 / n) ** 0.5
