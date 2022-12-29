# 1931 - 회의실 배정
import sys 
input = sys.stdin.readline
import heapq


N = int(input().rstrip())
data = []
for _ in range(N):
    start, end = map(int, input().rstrip().split())
    data.append((start, end))

data.sort(key=lambda x:x[0])
data.sort(key=lambda x:x[1])

now = data[0][1]
answer = 1

for x in data[1:]:
    if x[0] < now:
        continue
    else:
        now = x[1]
        answer += 1

print(answer)

# heap 이용
# N = int(input().rstrip())
# data = []
# for _ in range(N):
#     start, end = map(int, input().rstrip().split())
#     heapq.heappush(data, (end, start))

# now, _ = heapq.heappop(data)
# answer = 1

# while data:
#     end, start = heapq.heappop(data)
#     if start < now:
#         continue
#     else:
#         now = end
#         answer += 1

# print(answer)
