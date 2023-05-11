# 1946 - 신입 사원
import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N = int(input())
    data = []
    for _ in range(N):
        a, b = map(int, input().split())
        data.append((a, b))
    data.sort(key=lambda x:x[1])
    score = data[0][0]

    cnt = 1
    for x in data[1:]:
        if x[0] < score:
            score = x[0]
            cnt += 1
    print(cnt)