# 2211 - 네트워크 복구
import sys
import heapq
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

INF = int(1e9)
distance = [INF] * (N + 1)
start = 1
distance[start] = 0
heap = []
arr = [0] * (N + 1)
heapq.heappush(heap, (0, 1))

while heap:
    dist, now = heapq.heappop(heap)

    if distance[now] < dist:
        continue
    
    for i in graph[now]:
        cost = dist + i[1]
        
        if distance[i[0]] > cost:
            distance[i[0]] = cost
            heapq.heappush(heap, (cost, i[0]))
            arr[i[0]] = now

print(len(arr) - arr.count(0))
for start, end in enumerate(arr):
    if start >= 2:
        print(start, end)