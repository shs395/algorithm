# 1041 - 주사위
N = int(input())
dice = list(map(int, input().split()))
# 인접 세 개
def get_three_min():
    temp = []
    temp_three_min = 300
    temp_min = 0
    for i in range(6):
        temp.append(i)
        temp.append(5 - i)
        temp_min += dice[i]
        for j in range(6):
            if j not in temp:
                temp.append(j)
                temp.append(5 - j)
                temp_min += dice[j]
                for k in range(6):
                    if k not in temp:
                        temp_min += dice[k]
                        temp_three_min = min(temp_min, temp_three_min)
                        temp_min -= dice[k]
                temp.pop()
                temp.pop()
                temp_min -= dice[j]
        temp = []
        temp_min -= dice[i]
    return temp_three_min

def get_two_min():
    temp = []
    temp_two_min = 300
    temp_min = 0
    for i in range(6):
        temp.append(i)
        temp.append(5 - i)
        temp_min += dice[i]
        for j in range(6):
            if j not in temp:
                temp_min += dice[j]
                temp_two_min = min(temp_min, temp_two_min)
                temp_min -= dice[j]
        temp = []
        temp_min -= dice[i]
    return temp_two_min
                
ans = 0
if N == 1:
    ans = sum(dice) - max(dice)
else:
    three_min = get_three_min()
    two_min = get_two_min()
    one_min = min(dice)
    ans = three_min * 4 + two_min * (8 * (N - 2) + 4) + one_min * ((5 * (N - 2) ** 2) + 4 * (N - 2))
print(ans)
# 총 3개 노출짜리 4개
# 3개 노출 4
# 2개 노출 8 * (N - 2) + 4
# 1개 노출 5 * (N - 2) ** 2 + 4 * (N - 2)
