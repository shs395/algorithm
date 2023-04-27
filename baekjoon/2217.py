# 2217 - 로프
N = int(input())
data = []
for _ in range(N):
    data.append(int(input()))

data.sort(reverse=True)
result = []

for j in range(N):
    result.append(data[j] * (j + 1))

print(max(result))