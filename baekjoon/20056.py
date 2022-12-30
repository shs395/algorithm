# 20056 - 마법사 상어와 파이어볼

# (이동 -> 2개 이상 있는 칸에서 나누기) * K 번 -> 질량의 합

import sys
input = sys.stdin.readline
N, M, K = map(int, input().rstrip().split())
# m, s, d, cnt, 
# table = [[[0, 0, 0, 0] for _ in range(N)] for _ in range(N)]
direction = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
fireballs = []

def move(r, c, s, d):
    r = (r + (direction[d][0] * s)) % N
    c = (c + (direction[d][1] * s)) % N
    return [r, c]

for _ in range(M):
    fireballs.append(list(map(int, input().rstrip().split())))

for _ in range(K):
    table = [[[0, 0, 0, 0] for _ in range(N)] for _ in range(N)]

    for fireball in fireballs:
        r, c, m, s, d = fireball
        r = r - 1
        c = c - 1
        moved_r, moved_c = move(r, c, s, d)
        temp = table[moved_r][moved_c]
        temp[0] += m
        temp[1] += s
        if temp[2] == 0:
            temp[2] = [d]
        else:
            temp[2].append(d)
            
        temp[3] += 1
        table[moved_r][moved_c] = temp

    new_fireballs = []

    for i in range(N):
        for j in range(N):
            if table[i][j][3] > 1:
                # 모두 홀수 or 짝수
                flag = ''
                for d in table[i][j][2]:
                    if flag == '':
                        if d % 2 == 0:
                            flag = 'even'
                        else:
                            flag = 'odd'
                    elif flag == 'even':
                        if d % 2 == 1:
                            flag = 'fail'
                    elif flag == 'odd':
                        if d % 2 == 0:
                            flag = 'fail'

                if flag == 'fail':
                    for idx in range(4):
                        if table[i][j][0] // 5 != 0:
                            new_fireballs.append([i + 1, j + 1, table[i][j][0] // 5, table[i][j][1] // table[i][j][3], idx * 2 + 1])
                else:
                    for idx in range(4):
                        if table[i][j][0] // 5 != 0:
                            new_fireballs.append([i + 1, j + 1, table[i][j][0] // 5, table[i][j][1] // table[i][j][3], idx * 2])

                
            elif table[i][j][3] == 1:
                new_fireballs.append([i + 1, j + 1, table[i][j][0], table[i][j][1], table[i][j][2][0]])
            
    fireballs = new_fireballs

answer = 0
for _, _, m, _, _ in fireballs:
    answer += m 

print(answer)