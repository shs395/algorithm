# 2 - 위에서 아래로
N = int(input())
data = []
for _ in range(N):
    data.append(int(input()))
print(*sorted(data, reverse=True))