# 1051 - 숫자 정사각형
N, M = map(int, input().split())
data = []
answer = 0
for _ in range(N):
    data.append(list(input()))

max_size = min(N, M)

for i in range(N):
    for j in range(M):
        for k in range(max_size):
            if i + k < N and j + k < M:
                if data[i][j] == data[i + k][j] and data[i][j] == data[i][j + k] and data[i][j] == data[i + k][j + k]:
                    if (k + 1) * (k + 1) > answer: answer = (k + 1) * (k + 1)

print(answer)
        
