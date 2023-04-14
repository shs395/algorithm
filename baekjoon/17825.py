# 17825 - 주사위 윷놀이
import sys
sys.setrecursionlimit(16)
INF = int(1e9)
dice = list(map(int, input().split()))
board = {
    0 : [2, 4, 6, 8, 10],
    2 : [4, 6, 8, 10, 12],
    4 : [6, 8, 10, 12, 14],
    6 : [8, 10, 12, 14, 16],
    8 : [10, 12, 14, 16, 18],
    10 : [-13, -16, -19, -25, -30],
    12 : [14, 16, 18, 20, 22],
    14 : [16, 18, 20, 22, 24],
    16 : [18, 20, 22, 24, 26],
    18 : [20, 22, 24, 26, 28],
    20 : [-22, -24, -25, -30, -35],
    22 : [24, 26, 28, 30, 32],
    24 : [26, 28, 30, 32, 34],
    26 : [28, 30, 32, 34, 36],
    28 : [30, 32, 34, 36, 38],
    30 : [-28, -27, -26, -25, -30],
    32 : [34, 36, 38, 40, INF],
    34 : [36, 38, 40, INF, INF],
    36 : [38, 40, INF, INF, INF],
    38 : [40, INF, INF, INF, INF],
    40 : [INF, INF, INF, INF, INF],
    -13 : [-16, -19, -25, -30, -35],
    -16 : [-19, -25, -30, -35, 40],
    -19 : [-25, -30, -35, 40, INF],
    -25 : [-30, -35, 40, INF, INF],
    -22 : [-24, -25, -30, -35, -0],
    -24 : [-25, -30, -35, 40, INF],
    -28 : [-27, -26, -25, -30, -35],
    -27 : [-26, -25, -30, -35, 40],
    -26 : [-25, -30, -35, 40, INF],
    -30 : [-35, 40, INF, INF, INF],
    -35 : [40, INF, INF, INF, INF],
}
piece : {
    'a' : 0,
    'b' : 0,
    'c' : 0,
    'd' : 0,
}
answer = 0
def dfs(now, score, pieces):
    # if now == 0:
    #     print(now, score, pieces)
    # elif now == 1:
    #     print(now, score, pieces)
    # elif now == 2:
    #     print(now, score, pieces)
    # elif now == 3:
    #     print(now, score, pieces)
    # elif now == 4:
    #     print(now, score, pieces)
    # elif now == 5:
    #     print(now, score, pieces)

    # print(now, score, pieces)
    if now == 10:
        global answer
        answer = max(answer, score)
        return 

    for i in range(4):
        new_pieces = pieces[:]
        tmp_score = score
        if new_pieces[i] != INF:
            x = board[new_pieces[i]][dice[now] - 1]
            if x in new_pieces:
                if x == INF:
                    if x != INF:
                        if x < 0:
                            tmp_score -= x
                        else:
                            tmp_score += x
                    new_pieces[i] = x
                    dfs(now + 1, tmp_score, new_pieces)
                else:
                    continue
            else:
                if x != INF:
                    if x < 0:
                        tmp_score -= x
                    else:
                        tmp_score += x
                new_pieces[i] = x
                dfs(now + 1, tmp_score, new_pieces)

dfs(0, 0, [0, 0, 0, 0])

print(answer)
