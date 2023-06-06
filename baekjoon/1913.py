# 1913 - 달팽이
N = int(input())
x = int(input())

direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
direction_cnt = 0
cnt = N
tmp_cnt = N
tmp_cnt_cnt = 1
now = N ** 2
data = [[0 for _ in range(N)] for _ in range(N)]
i = 0
j = 0
answer = 0
while now > 0:
    if now == x:
        answer = (i + 1, j + 1)
    data[i][j] = now
    now -= 1
    tmp_cnt -= 1

    if tmp_cnt == 0:
        tmp_cnt_cnt += 1
        direction_cnt += 1
        if tmp_cnt_cnt % 2 == 0:
            cnt -= 1
            tmp_cnt = cnt
        else:
            tmp_cnt = cnt 
    i = i + direction[direction_cnt % 4][0]
    j = j + direction[direction_cnt % 4][1]

for x in data:
    print(*x)
print(answer[0], answer[1])
