import math
def solution(enroll, referral, seller, amount):
    answer = []
    people_dict = dict()
    revenue_dict = dict()
    revenue_dict['center'] = 0
    
    for i in range(len(enroll)):
        revenue_dict[enroll[i]] = 0
        if referral[i] == '-':
            people_dict[enroll[i]] = [enroll[i], 'center']
        else:
            people_dict[enroll[i]] = [enroll[i], referral[i]]
            people_dict[enroll[i]].extend(people_dict[referral[i]][1:])
    
    for i in range(len(seller)):
        money = amount[i] * 100
        for people in people_dict[seller[i]]:
            revenue_dict[people] += money - (money // 10)
            money = money // 10
            if money == 0:
                break
    
    for x in enroll:
        answer.append(revenue_dict[x])
        
    return answer
