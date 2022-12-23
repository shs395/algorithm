# 6086 - 최대 유량
from collections import deque

def conv(c):
    if c.isupper():
        return ord(c) - 65
    else:
        return ord(c) - 71

def bfs(visited):
    queue = deque()
    queue.append(source)
    visited[source] = True

    while queue:
        now = queue.popleft()
        for next_node, value in enumerate(graph[now]):
            # if value > 0:
            #     print(next_node, value)
            if visited[next_node] == -1 and graph[now][next_node] > 0:
                # print(next_node, graph[now][next_node])
                visited[next_node] = now
                queue.append(next_node)
    
    if visited[sink] == -1:
        return True
    else:
        return False

def ek():
    total_flow = 0

    while True:
        visited = [-1] * 52
        if bfs(visited):
            break
        min_flow = int(1e9)
        # print(visited)
        idx = sink
        while idx != source:
            min_flow = min(min_flow, graph[visited[idx]][idx])
            idx = visited[idx]
        
        total_flow += min_flow

        idx = sink
        while idx != source:
            graph[visited[idx]][idx] -= min_flow
            graph[idx][visited[idx]] += min_flow
            idx = visited[idx]
            
    print(total_flow)


N = int(input())
graph = [[0] * 52 for _ in range(52)]
source = conv('A')
sink = conv('Z')

for _ in range(N):
    a, b, c = input().split()
    c = int(c)

    ca = conv(a)
    cb = conv(b)
    graph[ca][cb] += c
    graph[cb][ca] += c

# print(graph)

ek()

# A = 65
# Z = 90
# a = 97 
# z = 122