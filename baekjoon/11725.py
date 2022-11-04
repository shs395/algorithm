# 11725 - 트리의 부모 찾기
import sys
from collections import deque
input = sys.stdin.readline
N = int(input().rstrip())
arr = [[] for _ in range(N + 1)]
ans = [0 for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
for _ in range(N - 1):
    parent, child = map(int, input().rstrip().split())
    arr[parent].append(child)
    arr[child].append(parent)

queue = deque([])
for i in arr[1]:
    queue.append([1, i])
    visited[i] = True
visited[1] = True

while queue:
    parent, child = queue.popleft()
    ans[child] = parent
    for i in arr[child]:
        if visited[i] == False:
            queue.append([child, i])
            visited[i] = True

for i in range(2, len(ans)):
    print(ans[i])

