# 12015 - 가장 긴 증가하는 부분 수열 2
import bisect

n = int(input())
a = list(map(int, input().split()))
lis = []

for x in a:
    if len(lis) == 0:
        lis.append(x)
    else:
        if x > lis[-1]:
            lis.append(x)
        elif x < lis[-1]:
            lis[bisect.bisect_left(lis, x)] = x

print(len(lis))
