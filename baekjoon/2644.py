# 2644 - 촌수계산
n = int(input())
a, b = map(int, input().split())
m = int(input())
data = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
ans = 0
def dfs(graph, visited, node, count):
    # print(visited, count)
    global ans
    visited[node] = True
    for x in graph[node]:
        if visited[x] == False:
            if x == b:
                ans = count + 1
            dfs(graph, visited, x, count + 1)
        
for _ in range(m):
    x, y = map(int, input().split())
    data[x].append(y)
    data[y].append(x)

dfs(data, visited, a, 0)

if ans == 0:
    print(-1)
else:
    print(ans)