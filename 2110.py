# 2110 - 공유기 설치
import sys
input = sys.stdin.readline
N, C = map(int, input().split())
data = []
for _ in range(N):
    x = int(input())
    data.append(x)

data.sort()

start = 0
end = 1000000000
answer = 0

while start <= end:
    mid = (start + end) // 2
    count = 1
    current = data[0]

    for i in range(1, len(data)):
        if data[i] >= current + mid:
            count += 1
            current = data[i]

    if count >= C:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)