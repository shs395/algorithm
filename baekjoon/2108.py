# 2108 - 통계학
import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
data = []
for _ in range(N):
    data.append(int(input()))
data.sort()
print(round(sum(data) / N))
print(data[N // 2])
x = Counter(data).most_common()
if len(x) > 1:
    if x[0][1] == x[1][1]:
        print(x[1][0])
    else:
        print(x[0][0])
else:
    print(x[0][0])
print(data[-1] - data[0])
