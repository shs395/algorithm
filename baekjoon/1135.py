# 1135 - 뉴스 전하기
import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
data = list(map(int, input().split()))

time_list = [0] * N
indegree = [0] * N
possible_list = [[] for _ in range(N)]

for i in range(1, N):
    indegree[data[i]] += 1

queue = deque()

for i in range(1, N):
    if indegree[i] == 0:
        queue.append((i, data[i]))

while queue:
    now, parent = queue.popleft()
    possible_list[parent].append(time_list[now] + 1)

    indegree[parent] -= 1
    if indegree[parent] == 0:
        tmp = 0
        possible_list[parent].sort(reverse=True)
        for i in range(len(possible_list[parent])):
            tmp = max(tmp, possible_list[parent][i] + i)
        
        time_list[parent] = tmp
        
        if parent != 0:
            queue.append((parent, data[parent]))

print(time_list[0])


