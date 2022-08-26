# 11651 - 좌표 정렬하기 2
import sys
input = sys.stdin.readline

N = int(input())
data = []
for i in range(N):
    x, y = map(int, input().split())
    data.append([x, y])
data.sort(key=lambda x:x[0])
data.sort(key=lambda x:x[1])
for i in data:
    print(i[0], i[1])

