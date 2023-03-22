# 2109 - 순회강연
import heapq
n = int(input())
data = [[] for _ in range(10001)]
day = 0
max_d = 0
for _ in range(n):
    p, d = map(int, input().split())
    if d > max_d:
        max_d = d
    data[d].append(p)
    # data.append((p, d))
answer = 0
heap = []
before = max_d
for i in range(max_d, 0, -1):
    if len(data[i]) != 0:
        tmp = before - i
        for j in range(tmp):
            if heap:
                x = heapq.heappop(heap)
                answer += x
        before = i
        for j in data[i]:
            heapq.heappush(heap, -j)

for j in range(before):
    if heap:
        x = heapq.heappop(heap)
        answer += x


    
print(-answer)
