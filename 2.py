import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss
import nist

def bin_uniform():
    alpha = np.random.uniform()
    return 1 if alpha >= 0.5 else 0


def bin_normal():
    xi = np.random.normal()
    return 1 if xi >= 0 else 0


x = []
n = 10000
for i in range(n):
    x.append(bin_uniform())

file = open("input.txt", 'w')

for i in x:
    file.write(str(i) + ' ') 

file.close()

file = open("input.txt", 'r')

print("[zeroes, ones, s, p, success]: " + str(nist.test1(file.read(), n)))
print("[chisq, p, success]: " + str(nist.test2(file.read(), n)))
print("[zeroes, ones, prop, vobs, p, success]: " + str(nist.test3(file.read(), n)))