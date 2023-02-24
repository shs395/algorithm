# 1 - 모험가 길드
N = int(input())
data = list(map(int, input().split()))
answer = 0
data.sort()
group_cnt = 0
group_max = 0
for x in data:
    if group_cnt == 0:
        group_max = x
        group_cnt += 1
    else:
        group_max = max(x, group_max)
        group_cnt += 1
    
    if group_cnt == group_max:
        answer += 1
        group_cnt = 0
        group_max = 0
        
print(answer)