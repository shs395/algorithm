# 1760B - Atilla's Favorite Problem
# https://codeforces.com/contest/1760/problem/B
t = int(input())
for _ in range(t):
    n = int(input())
    data = list(input())
    data.sort()
    print(ord(data[-1]) - 96)
    
