def solution(topping):
    answer = 0
    a_dict = dict()
    b_dict = dict()
    a_set = set()
    b_set = set()
    for x in topping:
        if x in a_dict:
            a_dict[x] += 1
        else:
            a_dict[x] = 1
        
        if x not in b_dict:
            b_dict[x] = 0
        a_set.add(x)
    
    for i in range(len(topping) - 1, -1, -1):
        x = topping[i]
        b_dict[x] += 1
        b_set.add(x)
        a_dict[x] -= 1
        if a_dict[x] == 0:
            a_set.remove(x)
        
        if len(a_set) == len(b_set):
            answer += 1
    return answer
