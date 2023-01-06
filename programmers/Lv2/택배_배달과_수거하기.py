def solution(cap, n, deliveries, pickups):
    answer = 0
    delivery_list = []
    pickup_list = []
    
    d_sum = 0
    i = n - 1
    while i >= 0:
        if d_sum == 0 and deliveries[i] != 0:
            delivery_list.append(i + 1)
            
        if d_sum + deliveries[i] < cap:
            d_sum += deliveries[i]
            i -= 1
        elif d_sum + deliveries[i] == cap:
            d_sum = 0
            i -= 1
        elif d_sum + deliveries[i] > cap:
            deliveries[i] -= (cap - d_sum)
            d_sum = 0
            
    p_sum = 0
    i = n - 1   
    while i >= 0:
        if p_sum == 0 and pickups[i] != 0:
            pickup_list.append(i + 1)
            
        if p_sum + pickups[i] < cap:
            p_sum += pickups[i]
            i -= 1
        elif p_sum + pickups[i] == cap:
            p_sum = 0
            i -= 1
        elif p_sum + pickups[i] > cap:
            pickups[i] -= (cap - p_sum)
            p_sum = 0
    
    if len(delivery_list) == len(pickup_list):
        for i in range(max(len(delivery_list), len(pickup_list))):
            answer += max(delivery_list[i], pickup_list[i]) * 2
    elif len(delivery_list) > len(pickup_list):
        for i in range(len(pickup_list)):
            answer += max(delivery_list[i], pickup_list[i]) * 2
        for i in range(len(pickup_list), len(delivery_list)):
            answer += delivery_list[i] * 2
    else:
        for i in range(len(delivery_list)):
            answer += max(delivery_list[i], pickup_list[i]) * 2
        for i in range(len(delivery_list), len(pickup_list)):
            answer += pickup_list[i] * 2
        
    return answer
