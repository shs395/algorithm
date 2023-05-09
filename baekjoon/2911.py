# 2911 - 전화 복구
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
data = []
for _ in range(N):
    P, C = map(int, input().split())
    data.append((P, C))

data.sort(key=lambda x:x[0])

tmp = 0
answer = 0

for x in data:
    if x[1] > tmp:
        answer += (x[1] - tmp)
        tmp = x[1]
    else:
        tmp = x[1]

print(answer)