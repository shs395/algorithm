# 4 - 만들 수 없는 금액
N = int(input())
coins = list(map(int, input().split()))
coins.sort()
target = 1
for coin in coins:
    if target < coin:
        break
    target += coin

print(target)
    