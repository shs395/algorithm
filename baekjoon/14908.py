# 14908 - 구두 수선공
N = int(input())

data = []
answer = []

for i in range(1, N + 1):
    T, S = map(int, input().split())
    data.append((S / T, i))

data.sort(key=lambda x:x[0], reverse=True)

for x in data:
    answer.append(x[1])

print(*answer)