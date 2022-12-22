# 17144 - 미세먼지 안녕!
import sys
input = sys.stdin.readline

R, C, T = map(int, input().rstrip().split())
room = []
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
ac1 = ''
ac2 = ''

for _ in range(R):
    room.append(list(map(int, input().rstrip().split())))

for i in range(R):
    if room[i][0] == -1:
        ac1 = (i, 0)
        ac2 = (i + 1, 0)
        break
        
def move():
    global room
    new_room = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if room[i][j] == -1:
                continue
            amount = room[i][j] // 5
            for k in range(4):
                ni = di[k] + i
                nj = dj[k] + j
                if 0 <= ni < R and 0 <= nj < C and room[ni][nj] != -1:
                    new_room[ni][nj] += amount
                    room[i][j] -= amount
            new_room[i][j] += room[i][j]
    new_room[ac1[0]][0] = -1
    new_room[ac2[0]][0] = -1
    room = new_room

def wind():
    for i in range(ac1[0] - 1, 0, -1):
        room[i][0] = room[i - 1][0]

    for j in range(C - 1):
        room[0][j] = room[0][j + 1]

    for i in range(ac1[0]):
        room[i][-1] = room[i + 1][-1]
    
    for j in range(C - 1, 0, -1):
        if j == 1:
            room[ac1[0]][j] = 0
        else:
            room[ac1[0]][j] = room[ac1[0]][j - 1]

def wind_btm():
    for i in range(ac2[0] + 1, R - 1):
        room[i][0] = room[i + 1][0]

    for j in range(C - 1):
        room[-1][j] = room[-1][j + 1]

    for i in range(R - 1, ac2[0], -1):
        room[i][-1] = room[i - 1][-1]

    for j in range(C - 1, 0, -1):
        if j == 1:
            room[ac2[0]][j] = 0
        else:
            room[ac2[0]][j] = room[ac2[0]][j - 1]

for _ in range(T):
    move()
    wind()
    wind_btm()

ans = 0
for x in room:
    ans += sum(x)

print(ans + 2)