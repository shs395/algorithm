# 1339 - 단어 수학
N = int(input())
data = [0 for _ in range(26)]
ans = 0
for _ in range(N):
    word = input()
    cnt = 0
    for c in word[::-1]:
        data[ord(c) - 65] += pow(10, cnt)
        cnt += 1

data.sort(reverse=True)
idx = 9
for x in data:
    if x == 0:
        break
    else:
        ans += idx * x
        idx -= 1
    

print(ans)