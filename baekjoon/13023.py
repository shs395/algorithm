# 13023 - ABCDE
import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
graph = [[] for _ in range(N)]
visited = [False for _ in range(N)]
cnt = 0
def dfs(node, count):
    visited[node] = True
    global cnt
    if count >= 4:
        cnt = 1
    if cnt == 1:
        return
    for n in graph[node]:
        if visited[n] == False:
            dfs(n, count + 1)
    
    visited[node] = False

for _ in range(M):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N):
    if visited[i] == False:
        dfs(i, 0)

print(cnt)