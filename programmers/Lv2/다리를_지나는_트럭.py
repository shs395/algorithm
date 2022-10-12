from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge_queue = deque([0 for _ in range(bridge_length)])
    truck_weights = deque(truck_weights)
    bridge_weight_sum = 0
    while True:
        if len(truck_weights) == 0 and bridge_weight_sum == 0:
            break
        next_truck = 0
        bridge_weight_sum -= bridge_queue.popleft()
        if len(truck_weights) != 0:
            if bridge_weight_sum + truck_weights[0] <= weight:
                next_truck = truck_weights.popleft()        
        bridge_queue.append(next_truck)
        bridge_weight_sum += next_truck
        time += 1
    return time
