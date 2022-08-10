# 2164 - 카드2
from collections import deque

N = int(input())
cards = [i for i in range(1, N + 1)]
queue = deque(cards)
            
while len(queue) != 1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue[0])
