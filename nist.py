
import math
def test1(input, n):
        
    ones = input.count('1') #number of ones

    zeroes = input.count('0')    #number of zeros

    s = abs(ones - zeroes)  

    p = math.erfc(float(s)/(math.sqrt(float(n)) * math.sqrt(2.0))) #p-value

    success = ( p >= 0.01)  # success = true if p-value >= 0.01

    return [zeroes, ones, s, p, success]

import math
import scipy.special as sc
from fractions import Fraction

def test2(input, n, M=32):
    # Compute number of blocks M = block size. N=num of blocks
    # N = floor(n/M)
    # miniumum block size 20 bits, most blocks 100
    # fieldnames = ['number','chisq','p-value', 'success']
    
    N = int(math.floor(n/M))
    
    if N > 99:
        N=99
        M = int(math.floor(n/N))

    if n < 100:
        # Too little data for test. Input of length at least 100 bits required
        return [0.0, 0.0, False]

    num_of_blocks = N

    block_size = M 

    proportions = list()

    for i in range(num_of_blocks):
        
        block = input[i*(block_size):((i+1)*(block_size))]
        
        ones = block.count('1')

        zeroes = block.count('0') 
        
        proportions.append(Fraction(ones,block_size))

    chisq = 0.0

    for prop in proportions:
        chisq += 4.0*block_size*((prop - Fraction(1,2))**2)
    
    p = sc.gammaincc((num_of_blocks/2.0),float(chisq)/2.0) # p-value
    success = (p>= 0.01)

    return [chisq, p, success]

def test3(input, n):
            
    ones = input.count('1') #number of ones

    zeroes = input.count('0')    #number of zeros

    prop = float(ones)/float(n)

    tau = 2.0/math.sqrt(n)

    vobs = 0.0

    if abs(prop-0.5) > tau:
        p = 0
    else:

        vobs = 1.0
        for i in range(n-1):
            if input[i] != input[i+1]:
                vobs += 1.0

        p = math.erfc(abs(vobs - (2.0*n*prop*(1.0-prop)))/(2.0*math.sqrt(2.0*n)*prop*(1-prop) ))
    
    success = (p>=0.01)


    return [zeroes, ones, prop, vobs, p, success]
