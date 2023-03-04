# 2568 - 전깃줄 - 2
import sys
input = sys.stdin.readline
import bisect

t = int(input().rstrip())
data = [-1] * 500001
idx_data = [-1] * 500001
lis = []
for _ in range(t):
    a, b = map(int, input().rstrip().split())
    data[a] = b

for i in range(1, 500001):
    if data[i] != -1:
        if len(lis) == 0:
            lis.append(data[i])
            idx_data[i] = 0
        else:
            if data[i] > lis[-1]:
                lis.append(data[i])
                idx_data[i] = len(lis) - 1
            else:
                tmp = bisect.bisect_left(lis, data[i])
                idx_data[i] = tmp
                lis[tmp] = data[i]

print(t - len(lis))
start = len(lis) - 1
answer = []
for i in range(500000, -1, -1):
    if idx_data[i] != -1:
        if idx_data[i] != start:
           answer.append(i) 
        elif idx_data[i] == start:
            start -= 1
answer.sort()
for x in answer:
    print(x)

