# 14003 - 가장 긴 증가하는 부분 수열 5
import bisect 
from collections import deque

N = int(input())
a = list(map(int, input().split()))
lis = [a[0]]
lis_len = 1
idx_list = [0] * (N)

for i in range(1, N):
    if a[i] > lis[-1]:
        lis.append(a[i])
        lis_len += 1
        idx_list[i] = lis_len - 1
    elif a[i] == lis[-1]:
        idx_list[i] = lis_len - 1
    else:
        tmp = bisect.bisect_left(lis, a[i])
        lis[tmp] = a[i]
        idx_list[i] = tmp

print(lis_len)
idx = lis_len - 1
queue = deque()
for i in range(len(idx_list) - 1, -1, -1):
    if idx_list[i] == idx:
        idx -= 1
        queue.appendleft(a[i])

print(*list(queue))

