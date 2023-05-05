# 1826 - 연료 채우기
import sys, heapq
input = sys.stdin.readline

N = int(input())
data = []
heap = []
answer = 0

for _ in range(N):
    a, b = map(int, input().split())
    data.append((a, b))

data.sort(key=lambda x:x[0])

L, P = map(int, input().split())

for x in data:
    if P < x[0]:
        if len(heap) == 0:
            answer = -1
            break
        else:
            while heap:
                P -= heapq.heappop(heap)
                answer += 1
                if P >= x[0]:
                    break
            if P < x[0]:
                answer = -1
                break
    heapq.heappush(heap, -x[1])

if answer != -1:
    if P - sum(heap) < L:
        answer = -1
    else:
        if P < L:
            while heap:
                P -= heapq.heappop(heap)
                answer += 1
                if P >= L:
                    break

print(answer)