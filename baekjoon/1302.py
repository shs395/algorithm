# 1302 - 베스트셀러
from collections import Counter
N = int(input())
data = []
for _ in range(N):
    data.append(input())
data.sort()
print(Counter(data).most_common()[0][0])