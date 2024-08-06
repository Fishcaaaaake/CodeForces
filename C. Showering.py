#https://codeforces.com/contest/1999/problem/C

for t in range(int(input())):
    n, s, m = map(int, input().split())
    ls, rs = [0]*n, [0]*n
    for _ in range(n):
        l, r = map(int, input().split())
        ls[_], rs[_] = l, r
    ls.sort()
    rs.sort()
    if(ls[0] >= s or m - rs[-1] >= s):
        print("YES")
        continue
    for i in range(n-1):
        if(ls[i+1] - rs[i] >= s):
            print("YES")
            break
    else:
        print("NO")