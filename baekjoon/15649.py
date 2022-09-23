# 15649 - N 과 M (1)
from itertools import combinations

def dfs(temp, visited, v, M):
    if len(temp) == M:
        print(" ".join(map(str, temp)))
        return
    else:
        for i in range(1, N + 1):
            if visited[i] == True:
                continue
            else:
                visited[i] = True
                temp.append(i)
                dfs(temp, visited, i, M)
                temp.pop()
                visited[i] = False
                    


N, M = map(int, input().split())
arr = [i for i in range(N + 1)]
visited = [False for i in range(N + 1)]
for i in range(1, N + 1):
    visited[i] = True
    dfs([i], visited, i, M)
    visited[i] = False

