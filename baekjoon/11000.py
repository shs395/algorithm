# 11000 - 강의실 배정
import sys, heapq
input = sys.stdin.readline

data = []
heap = []
answer = 0
N = int(input())
for _ in range(N):
    S, T = map(int, input().split())
    data.append([S, T])

data.sort(key=lambda x:x[0])

for i in data:
    if not heap:
        answer += 1
    else:
        if i[0] < heap[0]:
            answer += 1
        else:
            heapq.heappop(heap)
    heapq.heappush(heap, i[1])

print(answer)
