def solution(n, results):
    answer = 0
    INF = int(1e9)
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    
    for result in results:
        graph[result[0]][result[1]] = 1
        graph[result[1]][result[0]] = -1
    
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b:
                graph[a][b] = 0
    
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                if graph[a][b] == INF:
                    if graph[a][k] == 1 and graph[k][b] == 1:
                        graph[a][b] = 1
                    if graph[a][k] == -1 and graph[k][b] == -1:
                        graph[a][b] = -1
                
    for i in graph:
        if INF not in i[1:]:
            answer += 1
    return answer
