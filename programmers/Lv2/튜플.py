def solution(s):
    answer = []
    s = s[2:-2]
    s = s.split('},{')
    s.sort(key=lambda x:len(x))
    for i in s:
        temp = i.split(',')
        for t in temp:
            if int(t) not in answer:
                answer.append(int(t))
    return answer
