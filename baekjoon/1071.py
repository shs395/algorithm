# 1071 - 소트
import heapq

N = int(input())
data = list(map(int, input().split()))
data.sort()
answer = []
heap = []
max_data = max(data)
cnt = 0

for x in data:
    if len(answer) == 0 or answer[-1] == x:
        if x == max_data - 1:
            cnt += 1
        else:
            answer.append(x)
    else:
        if x > answer[-1] + 1:
            if x == max_data - 1:
                if heap:
                    answer.append(x)
                    while heap:
                        answer.append(heapq.heappop(heap))
                else:
                    cnt += 1
            else:
                answer.append(x)
                if heap and heap[0] != max_data - 1:
                    while heap:
                        answer.append(heapq.heappop(heap))
        else:
            heapq.heappush(heap, x)

while heap:
    answer.append(heapq.heappop(heap))

for _ in range(cnt):
    answer.append(max_data -1)

print(*answer)