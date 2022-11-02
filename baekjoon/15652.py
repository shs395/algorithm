# 15652 - N과 M(4)
from itertools import combinations_with_replacement
N, M = map(int, input().split())
arr = [i for i in range(1, N + 1)]
for i in list(combinations_with_replacement(arr, M)):
    for j in i:
        print(j, end=' ')
    print()
