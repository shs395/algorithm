# 5 - 볼링공 고르기
N, M = map(int, input().split())
data = list(map(int, input().split()))

answer = 0
for i in range(len(data)):
    tmp = data[i]
    for j in range(i + 1, len(data)):
        if data[j] != tmp:
            answer += 1

print(answer)