# 2677 - 단지번호붙이기
N = int(input())
data = []
ans = []
cnt = 0
visited = [[False for _ in range(N)] for _ in range(N)]
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
for _ in range(N):
    data.append(list(input()))

def dfs(i, j):
    global cnt
    visited[i][j] = True
    if data[i][j] == '1':
        cnt += 1
    for idx in range(4):
        ni = di[idx] + i
        nj = dj[idx] + j
        if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == False and data[ni][nj] == '1':
            dfs(ni, nj)

for i in range(N):
    for j in range(N):
        if data[i][j] == '1' and visited[i][j] == False:
            dfs(i, j)
            ans.append(cnt)
            cnt = 0

ans.sort()
print(len(ans))
for a in ans:
    print(a)