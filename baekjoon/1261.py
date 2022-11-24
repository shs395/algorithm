# 1261 - 알고스팟
# 막혀있다면 거리가 1이고 뚫려있다면 거리가 0임

# 0-1 BFS 문제
# 0 짜리는 덱에 앞에 넣고 1짜리는 뒤에 넣음 -> 0짜리부터 탐색하게 됨


from collections import deque
M, N = map(int, input().split())
graph = []
visited = [[False for _ in range(M)] for _ in range(N)]
for _ in range(N):
    graph.append(list(map(int, list(input()))))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque([])
queue.append((0, 0))
visited[0][0] = True
while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < M and 0 <= ny < N and visited[ny][nx] == False:
            visited[ny][nx] = True
            if graph[ny][nx] == 1:
                graph[ny][nx] = graph[y][x] + 1
                queue.append((nx, ny))
            else:
                graph[ny][nx] = graph[y][x]
                queue.appendleft((nx, ny))
            


print(graph[-1][-1])