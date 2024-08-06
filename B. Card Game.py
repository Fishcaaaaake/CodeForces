#https://codeforces.com/contest/1999/problem/B

def game(a, b):
    if(a > b): return 1
    if(a < b): return -1
    return 0


for t in range(int(input())):
    a1, a2, b1, b2 = map(int, input().split())
    sun_wins = 0
    if(game(a1, b1) + game(a2, b2) > 0): sun_wins += 2
    if(game(a1, b2) + game(a2, b1) > 0): sun_wins += 2
    print(sun_wins)