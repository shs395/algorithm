# 16236 - 아기 상어
from collections import deque
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def bfs(i, j):
    global shark_cnt, fish, shark, answer, shark_i, shark_j
    visited = [[-1] * N for _ in range(N)]
    queue = deque()
    queue.append((i, j, 0))
    visited[i][j] = 0

    fish_i = i
    fish_j = j
    dist = 500

    while queue:
        temp_i, temp_j, temp_dist = queue.popleft()
        
        if 0 < space[temp_i][temp_j] < shark:
            # if temp_dist > dist:
            #     continue
            if temp_dist != 0 and temp_dist < dist:
                dist = temp_dist
                fish_i = temp_i
                fish_j = temp_j
            elif temp_dist == dist:
                # 더 위에 있는 경우
                if temp_i < fish_i:
                    fish_i = temp_i
                    fish_j = temp_j
                # 가장 위에 있는 물고기들이 여러개
                elif temp_i == fish_i:
                    if temp_j < fish_j:
                        fish_i = temp_i
                        fish_j = temp_j
        
        # print(temp_i, temp_j, temp_dist, fish_i, fish_j, space[temp_i][temp_j], shark)

        for idx in range(4):
            ni = temp_i + di[idx]
            nj = temp_j + dj[idx]

            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == -1 and space[ni][nj] <= shark:
                visited[ni][nj] = temp_dist + 1
                queue.append((ni, nj, temp_dist + 1))

    # print(fish_i, fish_j,space[fish_i][fish_j])
    # print(fish[space[fish_i][fish_j] - 1])
    if fish_i == i and fish_j == j:
        return False
    fish[space[fish_i][fish_j] - 1] -= 1
    space[fish_i][fish_j] = 0
    space[shark_i][shark_j] = 0
    shark_cnt += 1
    if shark_cnt == shark:
        shark_cnt = 0
        shark += 1
    shark_i = fish_i
    shark_j = fish_j
    answer += visited[fish_i][fish_j]
    # print(visited)
        


N = int(input())
space = []
for _ in range(N):
    space.append(list(map(int, input().split())))

# print(space)
fish = [0, 0, 0, 0, 0, 0]
shark_i = 0
shark_j = 0
shark = 2
shark_cnt = 0
answer = 0

for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            shark_i = i
            shark_j = j
        elif space[i][j] == 0:
            continue
        else:
            fish[space[i][j] - 1] += 1

while True:
    # 먹을 수 있는 물고기 x
    # print(fish, fish[:shark - 1].count(0), shark - 1)
    if shark <= 7:
        if fish[:shark - 1].count(0) == shark - 1:
            break
        else:
            if bfs(shark_i, shark_j) == False:
                break
    else:
        if fish.count(0) == 6:
            break
        else:  
            if bfs(shark_i, shark_j) == False:
                break

    # 있는 경우
    
    # print('answer  :', answer)

print(answer)

    
