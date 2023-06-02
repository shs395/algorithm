# 9375 - 패션왕 신해빈
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    data = dict()
    for _ in range(n):
        a, b = input().rstrip().split()
        if b in data:
            data[b].append(a)
        else:
            data[b] = [a]
    answer = 1
    for x in data:
        answer *= (len(data[x]) + 1)
    print(answer - 1)

