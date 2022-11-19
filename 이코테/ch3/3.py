# 3 - 숫자 카드 게임

# 내 풀이
N, M = map(int, input().split())
cards = []
ans = -1
for _ in range(N):
    ans = max(min(list(map(int, input().split()))), ans)

print(ans)