# 1507 - 궁금한 민호
import copy
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
INF = int(1e9)
cp_graph = copy.deepcopy(graph)
break_flag = False
answer = 0

for k in range(N):
    if break_flag:
        break
    for a in range(N):
        if break_flag:
            break
        for b in range(N):
            if a == k or b == k:
                continue
            # 같다면, 그 길 쓴 것
            if graph[a][k] + graph[k][b] == graph[a][b]:
                cp_graph[a][b] = 0
                # print(graph[a][k], graph[k][b])
            # 크다면 길은 존재하나 쓰지는 않았음
            elif graph[a][k] + graph[k][b] > graph[a][b]:
                continue
            # 작은 것은 말이 안됨
            elif graph[a][k] + graph[k][b] < graph[a][b]:
                answer = -1
                break_flag = True
                break

if not break_flag:
    for x in cp_graph:
        answer += sum(x)

print(answer // 2)