# 15666 - N과 M (12)
from itertools import combinations_with_replacement
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
x = list(set(combinations_with_replacement(arr, M)))
x.sort()
for i in x:
    print(*i)