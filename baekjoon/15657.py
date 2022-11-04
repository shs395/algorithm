# 15657 - N과 M (8)
from itertools import combinations_with_replacement
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
for i in list(combinations_with_replacement(arr, M)):
    print(*i)
