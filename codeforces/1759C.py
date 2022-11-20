# C -Thermostat
# https://codeforces.com/contest/1759/problem/C
import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    l, r, x = map(int, input().rstrip().split())
    a, b = map(int, input().rstrip().split())
    big = max(a, b)
    small = min(a, b)
    if big == small:
        print(0)
    elif big - small >= x:
        print(1)
    elif small - x >= l or big + x <= r:
        print(2)
    elif small + x <= r and big - x >= l: 
        print(3)
    else:
        print(-1)