# 2251 - 물통
from collections import deque
A, B, C = map(int, input().split())
a_water, b_water, c_water = 0, 0, C

answer = []
visited = []
visited.append([a_water, b_water, c_water])
queue = deque([[a_water, b_water, c_water]])
while queue:
    # a, b, c
    temp = queue.popleft()
    a_water = temp[0]
    b_water = temp[1]
    c_water = temp[2]
    if a_water == 0 and c_water not in answer:
        answer.append(c_water)
    a_left = A - a_water
    b_left = B - b_water
    c_left = C - c_water
    # a, b
    if [a_water - min(a_water, b_left), b_water + min(a_water, b_left), c_water] not in visited:
        visited.append([a_water - min(a_water, b_left), b_water + min(a_water, b_left), c_water])
        queue.append([a_water - min(a_water, b_left), b_water + min(a_water, b_left), c_water])
    # a, c
    if [a_water - min(a_water, c_left), b_water, c_water + min(a_water, c_left)] not in visited:
        visited.append([a_water - min(a_water, c_left), b_water, c_water + min(a_water, c_left)])
        queue.append([a_water - min(a_water, c_left), b_water, c_water + min(a_water, c_left)])
    # b, a
    if [a_water + min(b_water, a_left), b_water - min(b_water, a_left), c_water] not in visited:
        visited.append([a_water + min(b_water, a_left), b_water - min(b_water, a_left), c_water])
        queue.append([a_water + min(b_water, a_left), b_water - min(b_water, a_left), c_water])
    # b, c
    if [a_water, b_water - min(b_water, c_left), c_water - min(b_water, c_left)] not in visited:
        visited.append([a_water, b_water - min(b_water, c_left), c_water - min(b_water, c_left)])
        queue.append([a_water, b_water - min(b_water, c_left), c_water + min(b_water, c_left)])
    # c, a
    if [a_water + min(c_water, a_left), b_water, c_water - min(c_water, a_left)] not in visited:
        visited.append([a_water + min(c_water, a_left), b_water, c_water - min(c_water, a_left)])
        queue.append([a_water + min(c_water, a_left), b_water, c_water - min(c_water, a_left)])
    # c, b
    if [a_water, b_water + min(c_water, b_left), c_water - min(c_water, b_left)]not in visited:
        visited.append([a_water, b_water + min(c_water, b_left), c_water - min(c_water, b_left)])
        queue.append([a_water, b_water + min(c_water, b_left), c_water - min(c_water, b_left)])

answer.sort()
print(*answer)