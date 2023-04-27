# 2457 - 공주님의 정원
import sys
input = sys.stdin.readline

data = {
    1 : 0,
    2 : 31,
    3 : 58,
    4 : 89,
    5 : 119,
    6 : 150,
    7 : 180,
    8 : 211,
    9 : 242,
    10 : 272,
    11 : 303,
    12 : 333,
}

start_date = data[3] + 1
end_date = data[12] + 1
arr = []
answer = 0

N = int(input())
for _ in range(N):
    sm, sd, em, ed = map(int, input().split())
    tmp_start = data[sm] + sd
    tmp_end = data[em] + ed
    if tmp_end >= end_date:
        tmp_end = end_date
    if tmp_start <= start_date:
        tmp_start = start_date
    arr.append((tmp_start, tmp_end))


arr.sort(key=lambda x:x[0])
arr.sort(key=lambda x:x[1], reverse=True)
visited = [False] * N

s_date = start_date
while s_date < end_date:
    flag = False
    for i in range(len(arr)):
        if arr[i][0] <= s_date and visited[i] == False:
            flag = True
            visited[i] = True
            s_date = arr[i][1]
            answer += 1
            break
    
    if flag == False:
        answer = 0
        break

print(answer)
