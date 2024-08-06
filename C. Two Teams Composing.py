for t in range(int(input())):
    n = int(input()); a = list(map(int, input().split()))
    if(n == 1): print(0); continue
    max_rep, distint_cnt, d = 0, 0, dict()
    for skill in a:
        if(skill in d): d[skill] += 1; max_rep = max(max_rep, d[skill])
        else: d[skill] = 1; distint_cnt += 1
    if(distint_cnt == n): ans = 1
    elif(distint_cnt == max_rep): ans  = distint_cnt - 1
    else: ans = min(distint_cnt, max_rep)
    print(ans)