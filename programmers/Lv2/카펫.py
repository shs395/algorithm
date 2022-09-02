def solution(brown, yellow):
    WH = yellow + brown
    for H in range(1, WH // 2 + 1):
        if WH % H == 0:
            W = WH // H 
            if 2 * W + 2 * H - 4 == brown:
                answer = [max(H, W), min(H, W)]
    return answer
