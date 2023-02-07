def solution(skill, skill_trees):
    answer = 0
    data = dict()
    for s in skill:
        data[s] = ''
    
    for s in skill_trees:
        temp = ''
        for x in s:
            if x in data:
                temp += x
        
        if temp == skill[:len(temp)]:
            answer += 1
    return answer
