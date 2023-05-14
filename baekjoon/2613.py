# 2613 - 숫자구슬
import sys, math
input = sys.stdin.readline
N, M = map(int, input().split())
data = list(map(int, input().split()))
start = min(data)
end = sum(data)
answer = int(1e9)
answer_cnt = []

while start <= end:
    mid = (start + end) // 2
    tmp = 0
    group_cnt = 1
    max_val = 0
    marble_cnt = 0
    tmp_marble_answer = []
    
    for x in data:
        if tmp + x > mid:
            group_cnt += 1
            tmp = x
            tmp_marble_answer.append(marble_cnt)
            marble_cnt = 1
        else:
            tmp += x
            marble_cnt += 1
    if marble_cnt:
        tmp_marble_answer.append(marble_cnt)

    if group_cnt <= M and max(data) <= mid:
        answer_cnt = tmp_marble_answer
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

while len(answer_cnt) < M:
    for i in range(len(answer_cnt)):
        if answer_cnt[i] > 1:
            tmp = answer_cnt[i]
            del answer_cnt[i]
            answer_cnt.insert(i, math.ceil(tmp/2))
            answer_cnt.insert(i, math.floor(tmp/2))
            if len(answer_cnt) == M:
                break
        
        
print(answer)
print(*answer_cnt)
