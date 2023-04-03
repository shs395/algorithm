# 9466 - 텀 프로젝트
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000000)

def dfs(visited, data, now, stack, answer):
    visited[now] = True
    stack.append(now)

    if visited[data[now]] == True:
        if data[now] in stack:
            for x in stack[stack.index(data[now]):]:
                answer[x] = True
    else:
        dfs(visited, data, data[now], stack, answer)
            

T = int(input())
for _ in range(T):
    n = int(input())
    data = [0]
    data.extend(list(map(int, input().split())))
    visited = [False] * (n + 1)
    answer = [False] * (n + 1)
    for i in range(1, len(data)):
        if visited[i] == False:
            stack = []
            dfs(visited, data, i, stack, answer)
    print(answer.count(False) - 1)
    