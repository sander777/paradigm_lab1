import numpy as np
import random
from datetime import datetime

class Circle:
    def __init__(self, o, r: np.array):
        self.o = np.array(o)
        self.r = r

    def is_in(self, p):
        d = 0
        for i in range(len(self.o)):
            d += (self.o[i] - p[i]) ** 2
        d **= 0.5
        return d <= self.r



class Field:
    def __init__(self):
        self.x1 = None
        self.x2 = None
        self.circles = list()
        

    def add_circle(self, c):
        self.circles.append(c)
        if len(self.circles) == 1:
            self.x1 = c.o + c.r
            self.x2 = c.o - c.r
            self.n = len(self.x1)
        else:
            for i in range(len(c.o)):
                if c.o[i] + c.r > self.x1[i]:
                    self.x1[i] = c.o[i] + c.r
                if c.o[i] + c.r < self.x2[i]:
                    self.x2[i] = c.o[i] - c.r

    def get_V(self, n):
        v = 0
        random.seed()
        rand = [0] * self.n
        for i in range(n):
            for j in range(self.n):
                rand[j] = random.uniform(self.x2[j], self.x1[j])
            b = True
            for j in self.circles:
                if not j.is_in(rand):
                    b = False
                    break
            if b:
                v += 1
        v /= n
        for i in (self.x1 - self.x2):
            v *= i
        return v


c = Circle([2, -1], 3)

c1 = Circle([1, 2], 2)

f = Field()

f.add_circle(c)
f.add_circle(c1)
print(f.get_V(1000000))