# 10974 - 모든 순열
from itertools import permutations 
N = int(input())
x = [i for i in range(1, N + 1)]
for y in list(permutations(x, N)):
    print(*y)