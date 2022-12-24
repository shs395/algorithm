# 15683 - 감시

# cctv 8개 -> 3, 4번 : 4가지 경우의수 -> 4 ^ 8 == 65536
# 칸 최대 64 
# 65536 * 64 == 419,4304
import copy

def watch(x, y, directions, temp_room):
    for direction in directions:
        if direction == 1:
            for i in range(x - 1, -1, -1):
                if temp_room[i][y] == 6:
                    break
                temp_room[i][y] = '#'
        elif direction == 2:
            for i in range(y + 1, M):
                if temp_room[x][i] == 6:
                    break
                temp_room[x][i] = '#'
        elif direction == 3:
            for i in range(x + 1, N):
                if temp_room[i][y] == 6:
                    break
                temp_room[i][y] = '#'
        elif direction == 4:
            for i in range(y - 1, -1, -1):
                if temp_room[x][i] == 6:
                    break
                temp_room[x][i] = '#'


def dfs(depth, room):
    global answer 

    if depth == len(cctv_list):
        cnt = 0
        for i in room:
            cnt += i.count(0)
        answer = min(answer, cnt)
        return

    x, y, cctv = cctv_list[depth]
    for directions in cctv_directions[cctv]:
        temp_room = copy.deepcopy(room)
        watch(x, y, directions, temp_room)
        dfs(depth + 1, temp_room)
    
N, M = map(int, input().split())
room = []
# 방향 북,동,남,서 1, 2 3, 4
cctv_directions = [
    [], 
    [[1], [2], [3], [4]], 
    [[1, 3], [2, 4]],
    [[1, 2], [2, 3], [3, 4], [4, 1]], 
    [[1, 2, 4], [1, 2, 3], [2, 3, 4], [3, 4, 1]],
    [[1, 2, 3, 4]]
]
cctv_list = []
answer = 65

for _ in range(N):
    room.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        if room[i][j] == 0 or room[i][j] == 6 or room[i][j] == '#':
            continue
        else:
            cctv_list.append([i, j, room[i][j]])
            
dfs(0, room)
print(answer)