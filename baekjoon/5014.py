# 5014 - 스타트링크
from collections import deque
F, S, G, U, D = map(int, input().split())
building = [False for _ in range(F + 1)]
count = 0
queue = deque([[S, count]])
building[S] = True
while queue:
    cur_f, temp_count = queue.popleft()
    if cur_f == G:
        count = temp_count
        break
    if cur_f + U <= F and building[cur_f + U] == False:
        queue.append([cur_f + U, temp_count + 1])
        building[cur_f + U] = True
    if cur_f - D > 0 and building[cur_f - D] == False:
        queue.append([cur_f - D, temp_count + 1])
        building[cur_f - D] = True

if G == S:
    print(0)
elif count == 0:
    print("use the stairs")
else:
    print(count)