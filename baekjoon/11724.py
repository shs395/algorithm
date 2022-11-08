# 11724 - 연결 요소의 개수
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
N, M = map(int, input().rstrip().split())
graph = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
ans = 0
for _ in range(M):
    u, v = map(int, input().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(node):
    visited[node] = True
    for next_node in graph[node]:
        if visited[next_node] == False:
            dfs(next_node)
    return 1

for i in range(1, N + 1):
    if visited[i] == False:
        ans += dfs(i)

print(ans)