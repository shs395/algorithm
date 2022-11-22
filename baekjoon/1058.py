# 1058 - 친구
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(input()))
ans = [[0 for _ in range(N)] for _ in range(N)]
for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if graph[i][j] == 'Y' or (graph[i][k] == 'Y' and graph[k][j] == 'Y'):
                ans[i][j] = 1
result = 0
for i in range(N):
    count = 0
    for j in range(N):
        if ans[i][j] == 1:
            count +=1 
    result = max(result, count)
print(result)