def solution(k, room_number):
    answer = []
    data = dict()
    for room in room_number:
        if room not in data:
            data[room] = room + 1
            answer.append(room)
        else:
            next_room = data[room]
            temp = [room]
            while True:
                if next_room not in data:
                    data[next_room] = next_room + 1
                    for r in temp:
                        data[r] = next_room + 1
                    # data[room] = next_room + 1
                    answer.append(next_room)
                    break
                else:
                    temp.append(next_room)
                    next_room = data[next_room]
                    
    return answer

