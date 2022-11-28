def solution(n, stations, w):
    answer = 0
    idx = 1
    station = 0
    while idx <= n and station < len(stations):
        if stations[station] - w <= idx <= stations[station] + w:
            idx = stations[station] + w + 1
            station += 1
        elif idx < stations[station] - w:
            answer += 1
            idx = idx + (2 * w) + 1
        elif idx > stations[station] + w:
            station += 1
    
    if (n - idx + 1) % (2 * w + 1) == 0:
        answer += (n - idx + 1) // (2 * w + 1)
    else:
        answer += (n - idx + 1) // (2 * w + 1) + 1
    return answer