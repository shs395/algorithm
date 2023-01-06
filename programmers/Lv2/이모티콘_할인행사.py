from collections import deque

def bfs(user_sale, user_price, emoticons, data):
    
    queue = deque()
    for i in range(1, 5):
        # idx, 할인율, 전체 할인, 이모티콘 가입, 가격
        queue.append((0, i, str(i), 0, 0))
        
    while queue:
        idx, sale, total_sale, emoticon_plus, total_price = queue.popleft()
        
        if idx == len(emoticons):
            if total_price >= user_price:
                emoticon_plus = 1
                total_price = 0
                
            if total_sale in data.keys():
                data[total_sale][0] += emoticon_plus
                data[total_sale][1] += total_price
            else:
                data[total_sale] = [emoticon_plus, total_price]
            
            continue
        
        if sale * 10 >= user_sale:
            total_price += emoticons[idx] * (100 - sale * 10) // 100
        
        for i in range(1, 5):
            queue.append((idx + 1, i, total_sale + str(i), emoticon_plus, total_price))
        

def solution(users, emoticons):
    answer = []
    data = dict()
    for user_sale, user_price in users:
        bfs(user_sale, user_price, emoticons, data)
    
    answer_list = list(data.values())
    answer_list.sort(reverse=True, key=lambda x:x[1])
    answer_list.sort(reverse=True, key=lambda x:x[0])
    answer = answer_list[0]
        
    return answer
