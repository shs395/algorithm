# 1715 - 카드 정렬하기
import sys, heapq
input = sys.stdin.readline
N = int(input())
minheap = []
count = 0
for _ in range(N):
    heapq.heappush(minheap, int(input()))

while True:
    if len(minheap) == 1:
        break
    else:
        temp = heapq.heappop(minheap) + heapq.heappop(minheap)
        count += temp
        heapq.heappush(minheap, temp)

print(count)