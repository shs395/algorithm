# 2012 - 등수 매기기
import sys
input = sys.stdin.readline
N = int(input())
data = []
for _ in range(N):
    data.append(int(input()))

cnt = 1
data.sort()
answer = 0

for x in data:
    answer += abs(cnt - x)
    cnt += 1

print(answer)

