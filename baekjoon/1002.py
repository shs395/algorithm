# 1002 - 터렛
import sys
input = sys.stdin.readline
import math

T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        distance = math.sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2))
        if r1 + r2 > distance > abs(r2 - r1):
            print(2)
        elif r1 + r2 == distance or abs(r2 - r1) == distance:
            print(1)
        else:
            print(0)