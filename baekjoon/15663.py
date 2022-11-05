# 15663 - N과 M (9)
from itertools import permutations
N, M = map(int, input().split())
arr = list(map(int, input().split()))
x = list(set(permutations(arr, M)))
x.sort()
for i in x:
    print(*i)
