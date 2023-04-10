# 12738 - 가장 긴 증가하는 부분 수열 3
import bisect

A = int(input())
data = list(map(int, input().split()))
lis = []

for x in data:
    if len(lis) == 0:
        lis.append(x)
    else:
        if x > lis[-1]:
            lis.append(x)
        else:   
            lis[bisect.bisect_left(lis, x)] = x

print(len(lis))