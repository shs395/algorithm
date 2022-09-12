# 1202 - 보석 도둑
import sys
import heapq
input = sys.stdin.readline
N, K = map(int, input().split())
jewelry = []
bag = []

for i in range(N):
    M, V = map(int, input().split())
    heapq.heappush(jewelry, [M, V])

for i in range(K):
    bag.append(int(input()))

bag.sort()

temp = []
answer = 0
for i in bag:
    while jewelry and jewelry[0][0] <= i:
        heapq.heappush(temp, -jewelry[0][1])
        heapq.heappop(jewelry)
    
    if temp:
        answer -= heapq.heappop(temp)

print(answer)
