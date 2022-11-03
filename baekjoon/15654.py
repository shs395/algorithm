# 15654 - N과 M (5)
from itertools import permutations
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
for i in list(permutations(arr, M)):
    for j in i:
        print(j, end=' ')
    print()

