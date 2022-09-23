from itertools import product
from bisect import bisect_left, bisect_right
def solution(info, query):
    answer = []
    apply = dict()
    temp_list = list(product(
        ['-', 'cpp','java','python'], 
        ['-', 'backend', 'frontend'],
        ['-', 'junior', 'senior'], 
        ['-', 'chicken', 'pizza']  
    ))
    for j in temp_list:
        apply["".join(j)] = []

    for i in info:
        temp = i.split()
        temp_lang = ['-']
        temp_lang.append(temp[0])
        temp_job = ['-']
        temp_job.append(temp[1])
        temp_carrer = ['-']
        temp_carrer.append(temp[2])
        temp_food = ['-']
        temp_food.append(temp[3])
        temp_list2 = list(product(temp_lang, temp_job, temp_carrer, temp_food))
        for j in temp_list2:
            apply["".join(j)].append(int(temp[4]))
    
    for j in temp_list:
        apply["".join(j)].sort()
        
    for i in query:
        i = i.replace('and ', '')
        temp = i.split()
        q = ''.join([temp[0], temp[1], temp[2], temp[3]])
        if len(apply[q]) == 0:
            answer.append(0)
        else:
            answer.append(len(apply[q]) - bisect_left(apply[q], int(temp[4])))
            
    return answer
