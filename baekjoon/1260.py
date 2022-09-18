# 1260 - DFS와 BFS
import sys
input = sys.stdin.readline
from collections import deque

def dfs(graph, visited, v, answer_dfs):
    visited[v] = True
    answer_dfs.append(v)
    for node in graph[v]:
        if visited[node] == False:
            dfs(graph, visited, node, answer_dfs)

def bfs(graph, visited, v, answer_bfs):
    queue = deque([v])

    while queue:
        temp_v = queue.popleft()
        if visited[temp_v] == False:
            visited[temp_v] = True
            answer_bfs.append(temp_v)
            for node in graph[temp_v]:
                queue.append(node)
    

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N + 1):
    graph[i].sort()

visited_dfs = [False for _ in range(N + 1)]
answer_dfs = []
dfs(graph, visited_dfs, V, answer_dfs)

visited_bfs = [False for _ in range(N + 1)]
answer_bfs = []
bfs(graph, visited_bfs, V, answer_bfs)

for i in range(len(answer_dfs)):
    print(answer_dfs[i], end=" ")
print()
for i in range(len(answer_bfs)):
    print(answer_bfs[i], end=" ")
