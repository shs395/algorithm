# 2660 - 회장뽑기
from collections import deque
n = int(input())

user_list = [[] for _ in range(n + 1)]
score_list = [[0] * (n + 1) for _ in range(n + 1)]
answer = []
while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    user_list[a].append(b)
    user_list[b].append(a)

for i in range(1, n + 1):
    queue = deque([[i, 0]])
    score_list[i][i] = -1
    while queue:
        next_idx, score = queue.popleft()
        for friend in user_list[next_idx]:
            if score_list[i][friend] == 0:
                score_list[i][friend] = score + 1
                queue.append([friend, score + 1])

min_score = 999999
for i in range(1, n + 1):
    min_score = min(max(score_list[i]), min_score)

for i in range(1, n + 1):
    if max(score_list[i]) == min_score:
        answer.append(i)

print(min_score, len(answer))
answer.sort()
print(*answer)
        
