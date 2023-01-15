def solution(n, k, cmd):
    answer = ''
    answer_list = dict()
    linked_list = [[i, i - 1, i + 1] for i in range(n - 1)]
    linked_list.append([n - 1, n - 2, -1])
    stack = []
    idx = k
    for op in cmd:
        temp = op.split()
        if temp[0] == 'U':
            for i in range(int(temp[1])):
                idx = linked_list[idx][1]
                           
        elif temp[0] == 'D':
            for i in range(int(temp[1])):
                idx = linked_list[idx][2] 
                           
        elif temp[0] == 'C':
            if linked_list[idx][2] == -1:
                linked_list[linked_list[idx][1]][2] = -1
                stack.append(linked_list[idx])
                idx = linked_list[idx][1]
            elif linked_list[idx][1] == -1:
                linked_list[linked_list[idx][2]][1] = -1
                stack.append(linked_list[idx])
                idx = linked_list[idx][2]
            else:
                linked_list[linked_list[idx][1]][2] = linked_list[idx][2]
                linked_list[linked_list[idx][2]][1] = linked_list[idx][1]
                stack.append(linked_list[idx])
                idx = linked_list[idx][2]
                
        elif temp[0] == 'Z':
            recover = stack.pop()
            before_node = linked_list[recover[0]][1]
            next_node = linked_list[recover[0]][2]
            
            linked_list[before_node][2] = recover[0]
            if next_node != -1:
                linked_list[next_node][1] = recover[0]
            
    for s in stack:
        answer_list[s[0]] = ''
    
    for i in range(n):
        if i in answer_list:
            answer += 'X'
        else:
            answer += 'O'
        
            
    return answer
