# 10250 - ACM 호텔
import math
T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    floor = N % H
    num = N / H 
    if floor == 0:
        floor = H
    print(floor * 100 + math.ceil(num))