# 1461 - 도서관
from collections import deque
N, M = map(int, input().split())
books = list(map(int, input().split()))
minus_list = []
plus_list = []
ans = 0
for book in books:
    if book >= 0:
        plus_list.append(book)
    else:
        minus_list.append(book)

plus_list.sort(reverse=True)
minus_list.sort()

plus_list = deque(plus_list)
minus_list = deque(minus_list)

if len(plus_list) == 0 :
    ans += abs(minus_list[0])
    for _ in range(M):
        if minus_list:
            minus_list.popleft()
elif len(minus_list) == 0:
    ans += abs(plus_list[0])
    for _ in range(M):
        if plus_list:
            plus_list.popleft()
elif abs(minus_list[0]) >= abs(plus_list[0]):
    ans += abs(minus_list[0])
    for _ in range(M):
        if minus_list:
            minus_list.popleft()
elif abs(minus_list[0]) < abs(plus_list[0]):
    ans += abs(plus_list[0])
    for _ in range(M):
        if plus_list:
            plus_list.popleft()

while minus_list:
    ans += 2 * abs(minus_list[0])
    for _ in range(M):
        if minus_list:
            minus_list.popleft()
while plus_list:
    ans += 2 * abs(plus_list[0])
    for _ in range(M):
        if plus_list:
            plus_list.popleft()

print(ans)