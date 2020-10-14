import gauss5
import scipy.stats as ss

a_1 = []
a_2 = []

b_3 = []
b_12 = []
b_48 = []

for i in range(100000):
    a_1.append(gauss5.a_1())
    a_2.append(gauss5.a_2())
    b_3.append(gauss5.b(3))
    b_12.append(gauss5.b(12))
    b_48.append(gauss5.b(48))

print("a_1: " + str(ss.normaltest(a_1)))
print("a_2: " + str(ss.normaltest(a_2)))
print("b_3: " + str(ss.normaltest(b_3)))
print("b_12: " + str(ss.normaltest(b_12)))
print("b_48: " + str(ss.normaltest(b_48)))