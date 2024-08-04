from math import isqrt

def factorisations(n):
    factors = []
    for i in range(2, isqrt(n) + 1):
        if(not n%i):
            factors.append((i, n//i))
    return factors

for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    n_factors = factorisations(n)
    max_dif = max(a) - min(a) #considering k = n
    if(max_dif == 0):
        print(0)
        continue
    for factor_pair in n_factors:
        k1, k2 = factor_pair[0], factor_pair[1]
        weights1 = [sum(a[k1*i:k1*(i+1)]) for i in range(k2)]
        weights2 = [sum(a[k2*i:k2*(i+1)]) for i in range(k1)]
        max_dif = max(max_dif, max(weights1) - min(weights1), max(weights2) - min(weights2))
    print(max_dif)