# 2212 - 센서
import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
data = list(map(int, input().split()))
data.sort()

if K < N:
    tmp = []
    for i in range(1, len(data)):
        tmp.append(data[i] - data[i - 1])

    tmp.sort()

    for _ in range(K - 1):
        tmp.pop()

    print(sum(tmp))
else:
    print(0)