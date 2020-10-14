import numpy as np

def monte_carlo_integral(f, a, b, n=100):
    return (b - a) * np.mean(list(map(f, np.random.uniform(a, b, n))))

f1 = lambda x: x**7 + x**5 + x**3
f2 = lambda x: 2 * np.sin(3 * x)
f3 = lambda x: 1 / (x + 1) / x**0.5
print(monte_carlo_integral(f1, 0, 1, 1000000))
print(monte_carlo_integral(f2, 0, np.pi, 1000000))


f3_int = 0
step = 10
eps = 0.0001
i = 0
while True:
    I = monte_carlo_integral(f3, i * step, (i + 1) * step, 10000)
    if abs(I) < eps: break
    f3_int += I
    i += 1
print(f3_int)