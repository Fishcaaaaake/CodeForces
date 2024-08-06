#https://codeforces.com/contest/1999/problem/D

for _ in range(int(input())):
    s = list(input())
    t = input()
    i, j = 0, 0
    while(i < len(t) and j < len(s)):
        if(t[i] == s[j] or s[j] == '?'):
            s[j] = t[i]
            i += 1
        j += 1
    if(i < len(t)):
        print("NO")
        continue
    print("YES")
    print(''.join(s).replace('?', 'a'))