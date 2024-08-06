#https://codeforces.com/contest/1999/problem/E

def zerofication_steps(n):
    count = 0
    while(n >= 3):
        n //= 3
        count += 1
    return (count + 1) if n > 0 else count

psum = [0] * (2*10**5 + 1)
for i in range(1, 2*10**5 + 1):
    psum[i] = psum[i-1] + zerofication_steps(i)

for t in range(int(input())):
    l, r = map(int, input().split())
    steps = 2*zerofication_steps(l)
    steps += psum[r] - psum[l]
    print(steps)