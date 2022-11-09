# 1987 - 알파벳
# pypy3 통과 코드
# python3 통과하려면 bfs 사용
R, C = map(int, input().split())
graph = []
for _ in range(R):
    graph.append(list(input()))

visited = [[False for _ in range(C)] for _ in range(R)]
alphabet = [0 for _ in range(26)]
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

ans = 0
def dfs(r, c, cnt):
    global ans
    visited[r][c] = True
    alphabet[ord(graph[r][c]) - 65] = 1
    ans = max(ans, cnt)
    for i in range(4):
        nr = dr[i] + r
        nc = dc[i] + c
        if 0 <= nr < R and 0 <= nc < C and visited[nr][nc] == False:
            if alphabet[ord(graph[nr][nc]) - 65] == 0:
                dfs(nr, nc, cnt + 1)
    visited[r][c] = False
    alphabet[ord(graph[r][c]) - 65] = 0

dfs(0, 0, 1)

print(ans)