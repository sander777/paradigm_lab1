def is_prime(n: int):
    if n <= 1 or n % 2 == 0:
        return False
    boundry = n**0.5

    for i in range(3, int(boundry+1)):
        if n % i == 0:
            return False

    return True

def mersen_numbers(n):
    return (1 << n) - 1

def next_prime(n: int, N):
    k = 0
    num = n + 1
    res = []
    while k < N:
        if is_prime(num) and is_prime(num + 2):
            k += 1
            res.append(num)
        num += 1
    return res

def next_mesren(n: int, N):
    import math
    p = math.ceil(math.log2(n-1))
    res = []
    for i in range(N):
        res.append(mersen_numbers(p+i))
    return res

def print_next_primes(n, N):
    print("Next {} number(s) of type(N+-1) is prime bigger then {}:".format(N, n))
    for i in next_prime(n1, N):
        print("{} and {} ".format(i, i + 2))

def print_next_mersen(n, N):
    print("Next {} mersen numbers bigger then {}:".format(N, n))
    for i in next_mesren(n1, N):
        print(i)

n1 = 10**6
n2 = 10**9
n3 = 10**10
print_next_primes(n1, 3)
print_next_mersen(n1, 3)