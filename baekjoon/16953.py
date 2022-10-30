# 16953 - A -> B
from collections import deque
A, B = map(int, input().split())
count = -1
queue = deque([[A, 1]])
while queue:
    temp_num, temp_count = queue.popleft()
    if temp_num * 2 == B or temp_num * 10 + 1 == B:
        count = temp_count + 1
        break
    if temp_num * 2 < B:
        queue.append([temp_num * 2, temp_count + 1])
    if temp_num * 10 + 1 < B:
        queue.append([temp_num * 10 + 1, temp_count + 1])

print(count)