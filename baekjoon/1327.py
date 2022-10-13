# 1327 - 소트 게임
from collections import deque
N, K = map(int, input().split())
arr = list(input().split())

def list_to_str(arr):
    return ''.join(arr)

answer_str = list_to_str(sorted(arr))
answer = -1
count = 0
queue = deque([[list_to_str(arr), count]])
visited = dict()
visited[list_to_str(arr)] = 1
while queue:
    temp_str, temp_count = queue.popleft()
    if temp_str == answer_str:
        answer = temp_count
        break
    for i in range(len(arr) - K + 1):
        change_str = ''
        change_str = temp_str[:i] + temp_str[i:i + K][::-1] + temp_str[i + K:]
        if change_str not in visited:
            visited[change_str] = 1
            queue.append([change_str, temp_count + 1])
print(answer)

# visited 처리를 queue에서 뺄 때가 아니라 넣을 때 하자...
# visited를 리스트가 아니라 set이나 dict을 고려하자..
     

