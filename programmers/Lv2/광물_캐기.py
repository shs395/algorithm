def solution(picks, minerals):
    answer = 0
    data = {'diamond' : (1, 5, 25), 'iron' : (1, 1, 5), 'stone' : (1, 1, 1)}
    cnt = 0
    x = []
    tmp = [0, 0, 0]
    
    for mineral in minerals[:sum(picks) * 5]:
        for i in range(len(data[mineral])):
            tmp[i] += data[mineral][i]
        cnt += 1
        if cnt == 5:
            x.append(tmp)
            tmp = [0, 0, 0]
            cnt = 0
            
    x.append(tmp)
    x.sort(key=lambda x:x[2])
    
    for i in range(3):
        tmp = 0
        for _ in range(picks[i]):
            if x:
                tmp += x.pop()[i]
        answer += tmp
    return answer