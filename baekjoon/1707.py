# 1707 - 이분 그래프
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
K = int(input().rstrip())

def dfs(node, before):
    global ans
    visited[node] = before % 2 + 1
    for n in graph[node]:
        if visited[n] == 0:
            visited[n] == before
            dfs(n, before % 2 + 1)
        elif visited[n] == before:
            continue
        else:
            ans = 'NO'
            break

for _ in range(K):
    V, E = map(int, input().rstrip().split())
    graph = [[] for _ in range(V + 1)]
    visited = [0 for _ in range(V + 1)]
    ans = 'YES'
    for _ in range(E):
        u, v = map(int, input().rstrip().split())
        graph[u].append(v)
        graph[v].append(u)
    for i in range(1, V + 1):
        if visited[i] == 0:
            dfs(i, 1)
    print(ans)
    