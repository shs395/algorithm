# 9370 - 미확인 도착지
import sys
import heapq
input = sys.stdin.readline

def dijkstra(start):
    distance = [INF] * (n + 1) 
    distance[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))
    while heap:
        dist, now = heapq.heappop(heap)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))
    return distance

T = int(input().rstrip())
INF = int(1e9)
for _ in range(T):
    n, m, t = map(int, input().rstrip().split())
    s, g, h = map(int, input().rstrip().split())
    graph = [[] for _ in range(n + 1)]
   
    for _ in range(m):
        a, b, d = map(int, input().rstrip().split())
        graph[a].append((b, d))
        graph[b].append((a, d))

    distance = dijkstra(s)
    mid = 0
    if distance[g] > distance[h]:
        mid = g
    else:
        mid = h
    distance_mid = dijkstra(mid)

    answer = []
    for _ in range(t):
        x = int(input().rstrip())
        if distance[mid] + distance_mid[x] == distance[x]:
            answer.append(x)

    answer.sort()
    print(*answer)

    
    

