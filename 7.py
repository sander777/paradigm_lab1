import numpy as np
n=1000000
def generate_binaryrandom(ksi, n):
    i=0
    beta=[0]*n
    while i < n:
        beta[i]=(int)(ksi[i+1]-ksi[i]>0)
        i+=1
    return beta
 
ksi=np.random.normal(size=n+1)
binary_random=generate_binaryrandom(ksi, n)
ones=binary_random.count(1)
zeroes=binary_random.count(0)
print("Ones: " + str(ones))
print("Zeroes: " + str(zeroes))