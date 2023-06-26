# 1337 - 올바른 배열
N = int(input())
data = []
for _ in range(N):
    data.append(int(input()))
data.sort()
answer = 0

for i in range(N):
    cnt = 0
    for j in range(i + 1, N):
        if data[j] > data[i] + 4:
            break
        else:
            cnt += 1
    answer = max(answer, cnt)

print(4 - answer)