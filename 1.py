import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss


x = 25


def pseudo_random(x_=None):
    M = 27
    m = 2
    global x
    if x is float:
        x = x_
    x = x * M % (2**m) / (2**m)
    return x


l = 0.05
ranges = [0]*int(1 / l)
rand_list = list()
iterations = 20000
for i in range(iterations):
    ranges[int(pseudo_random() / l)] += 1
    rand_list.append(x)


plt.plot(list(np.arange(0, 1, l)), ranges)
plt.ylim(0, max(ranges) * 1.5)
plt.show()

