# 11509 - 풍선 맞추기
N = int(input())
H = list(map(int, input().split()))
data = [0 for _ in range(1000001)]
for i in range(len(H)):
    if data[H[i]] == 0:
        data[H[i] - 1] += 1
    else:
        data[H[i]] -= 1
        data[H[i] - 1] += 1

print(sum(data))