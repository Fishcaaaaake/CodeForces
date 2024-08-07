#https://codeforces.com/contest/1999/problem/F

MAX = 2*10**5
mod = 10 ** 9 + 7

fact = [1] * (MAX + 1)
inv_fact = [1] * (MAX + 1)

# Precomputing factorials
for i in range(1, MAX + 1):
    fact[i] = (fact[i - 1] * i) % mod

# Precomputing inverse factorials
inv_fact[MAX] = pow(fact[MAX], mod - 2, mod)
for i in range(MAX, 0, -1):
    inv_fact[i - 1] = (inv_fact[i] * i) % mod

def C(n, k):
    if k < 0 or k > n:
        return 0
    return (fact[n] * inv_fact[k] * inv_fact[n - k]) % mod

for t in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ones_count = a.count(1)
    ans = 0

    for i in range(k//2 + 1, ones_count + 1):
        ans += C(ones_count, i) * C(n - ones_count, k - i)
        ans %= mod

    print(ans)