# 14500 - 테트로미노
import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
paper = []
visited = [[False for _ in range(M)] for _ in range(N)]
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
ans = 0

for _ in range(N):
    paper.append(list(map(int, input().rstrip().split())))

max_val = -1
for x in paper:
    max_val = max(max_val, max(x))

def dfs(i, j, cnt, total):
    global ans

    if total  + max_val * (4 - cnt) <= ans:
        return 

    if cnt == 4:
        ans = max(ans, total)
        return 
 
    for idx in range(4):
        ni = i + di[idx]
        nj = j + dj[idx]
        if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == False:
            visited[ni][nj] = True
            dfs(ni, nj, cnt + 1, total + paper[ni][nj])
            visited[ni][nj] = False
            if cnt == 2:
                visited[ni][nj] = True
                dfs(i, j, cnt + 1, total + paper[ni][nj])
                visited[ni][nj] = False
            
       

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, 1, paper[i][j])
        visited[i][j] = False

print(ans)