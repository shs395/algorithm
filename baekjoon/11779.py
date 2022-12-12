# 11779 - 최소비용 구하기 2
import sys
import heapq
input = sys.stdin.readline

n = int(input().rstrip())
graph = [[] for _ in range(n + 1)]
m = int(input().rstrip())
INF = int(1e9)

for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b, c))

start, end = map(int, input().rstrip().split())

distance = [[INF, []] for _ in range(n + 1)] 
distance[start][0] = 0
distance[start][1] = [start]
heap = []
heapq.heappush(heap, (0, start, [start]))

while heap:
    dist, now, arr = heapq.heappop(heap)

    if distance[now][0] < dist:
        continue
    
    for i in graph[now]:
        cost = dist + i[1]

        if cost < distance[i[0]][0]:
            temp_arr = arr[:]
            distance[i[0]][0] = cost
            temp_arr.append(i[0])
            distance[i[0]][1] = temp_arr
            heapq.heappush(heap, (cost, i[0], temp_arr))

print(distance[end][0])
print(len(distance[end][1]))
print(*distance[end][1])