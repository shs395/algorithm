 def solution(dirs):
    answer = 0
    x = 0
    y = 0
    data = []
    for dir in dirs:
        if dir == 'U':
            if y < 5 :
                y += 1
                if [x, y - 1, x, y] not in data and [x, y, x, y - 1] not in data:
                    data.append([x, y - 1, x, y])
                    answer += 1
        elif dir == 'D':
            if y > -5:
                y -= 1
                if [x, y + 1, x, y] not in data and [x, y, x, y + 1] not in data:
                    data.append([x, y + 1, x, y])
                    answer += 1
        elif dir == 'R':
            if x < 5:
                x += 1
                if [x - 1, y, x, y] not in data and [x, y, x - 1, y] not in data:
                    data.append([x - 1, y, x, y])
                    answer += 1
        elif dir == 'L':
            if x > -5:
                x -= 1
                if [x + 1, y, x, y] not in data and [x, y, x + 1, y] not in data:
                    data.append([x + 1, y, x, y])
                    answer += 1
    print(data)
    return answer
