def solution(sticker):
    answer = 0
    if len(sticker) == 1:
        return sticker[0]
    elif len(sticker) == 2:
        return max(sticker[0], sticker[1])
    else:
        # 첫 번째를 선택하는 경우 
        dp1 = [0] * (len(sticker) - 1)
        # 첫 번째를 선택 안하는 경우
        dp2 = [0] * (len(sticker) - 1)

        for i in range(len(sticker) - 1):
            dp1[i] = max(dp1[i - 2] + sticker[i], dp1[i - 1])
            dp2[i] = max(dp2[i - 2] + sticker[i + 1], dp2[i - 1])
        return max(dp1[-1], dp2[-1])
