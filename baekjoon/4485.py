# 4485 - 녹색 옷 입은 애가 젤다지?
import heapq

di = [1, -1, 0, 0]
dj = [0, 0, -1, 1]
INF = int(1e9)
ii = 1
while True:
    N = int(input())
    if N == 0:
        break
    else:
        graph = []
        distance = [[INF for _ in range(N)] for _ in range(N)]

        for _ in range(N):
            graph.append(list(map(int, input().split())))

        heap = [(graph[0][0], 0, 0)]
        distance[0][0] = graph[0][0]

        while heap:
            dist, i, j = heapq.heappop(heap)

            for idx in range(4):
                ni = i + di[idx]
                nj = j + dj[idx]

                if 0 <= ni < N and 0 <= nj < N:
                    cost = dist + graph[ni][nj] 
                    if cost < distance[ni][nj]:
                        distance[ni][nj] = cost
                        heapq.heappush(heap, (cost, ni, nj))
    
        print(f'Problem {ii}: {distance[N - 1][N - 1]}')
        ii += 1
