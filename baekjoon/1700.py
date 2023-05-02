# 1700 - 멀티탭 스케줄링
import heapq
from collections import defaultdict, deque

N, K = map(int, input().split())
data = list(map(int, input().split()))
arr = set()
cnt = defaultdict(int)
queue_list = [deque() for _ in range(max(data) + 1)]
answer = 0

for idx, x in enumerate(data):
    cnt[x] += 1
    queue_list[x].append(idx)


for x in data:
    if len(arr) < N:
        cnt[x] -= 1
        queue_list[x].popleft()
        arr.add(x)
    elif len(arr) == N:
        if x in arr:
            cnt[x] -= 1
            queue_list[x].popleft()
            continue
        else:
            tmp = 10000
            target = 0
            tmp_next = -1

            for y in arr:
                if len(queue_list[y]) == 0: 
                    target = y
                    break
                else:
                    if queue_list[y][0] > tmp_next:
                        tmp_next = queue_list[y][0]
                        target = y

            arr.remove(target)
            cnt[x] -= 1
            queue_list[x].popleft()
            arr.add(x)
            answer += 1
print(answer)
            
