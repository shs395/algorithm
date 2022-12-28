# 2631 - 줄세우기
import sys
import bisect
input = sys.stdin.readline
N = int(input().rstrip())
data = []
for _ in range(N):
    data.append(int(input().rstrip()))


lis = [data[0]]

for x in data[1:]:
    if x > lis[-1]:
        lis.append(x)
    elif x < lis[-1]:
        lis[bisect.bisect_left(lis, x)] = x

print(N - len(lis))