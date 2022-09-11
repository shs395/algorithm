from itertools import permutations
import copy
def is_same(id1, id2):
    if len(id1) != len(id2):
        return False
    else:
        temp = 0
        for i in range(len(id1)):
            if id1[i] == '*':
                temp += 1
            else:
                if id1[i] == id2[i]:
                    temp += 1
                else:
                    break
        if temp == len(id1):
            return True
        else:
            return False
        
def solution(user_id, banned_id):
    answer = 0
    answer_list = []
    combi_list = list(permutations(user_id, len(banned_id)))
    for combi in combi_list:
        combi = list(combi)
        # print(combi)
        temp = []
        for id1 in banned_id:
            for id2 in combi:
                if id2 not in temp:
                    if is_same(id1, id2) == True:
                        temp.append(id2)
                        break
            if temp == combi:x
                temp.sort()
                if temp not in answer_list:
                    answer_list.append(temp)
                    answer += 1
    return answer
