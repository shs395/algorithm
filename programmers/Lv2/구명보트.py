def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    temp = [0]
    for person in people:
        if person <= temp[-1]:
            temp.pop()
        else:
            temp.append(limit - person)
            answer += 1
    return answer
