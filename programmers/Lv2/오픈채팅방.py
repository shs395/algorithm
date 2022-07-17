def solution(record):
    answer = []
    data = dict()
    for i in record:
        temp = i.split()
        if temp[0] == 'Enter' or temp[0] == 'Change':
            data[temp[1]] = temp[2]
    for i in record:
        temp = i.split()
        if temp[0] == 'Enter':
            answer.append(f'{data[temp[1]]}님이 들어왔습니다.')
        elif temp[0] == 'Leave':
            answer.append(f'{data[temp[1]]}님이 나갔습니다.')
    return answer
