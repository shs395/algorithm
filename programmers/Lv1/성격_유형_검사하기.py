def solution(survey, choices):
    answer = ''
    data = {'R': 0, 'T': 0, 'F' : 0, 'C' : 0, 'M' : 0, 'J' : 0, 'A' : 0, 'N' : 0}
    for i in range(len(survey)):
        if choices[i] <= 3:
            data[survey[i][0]] += -1 * (choices[i] - 4)
        elif choices[i] >= 5:
            data[survey[i][1]] += choices[i]  - 4\
    
    if data['R'] >= data['T']:
        answer += 'R'
    else:
        answer += 'T'
    if data['C'] >= data['F']:
        answer += 'C'
    else:
        answer += 'F'
    if data['J'] >= data['M']:
        answer += 'J'
    else:
        answer += 'M'
    if data['A'] >= data['N']:
        answer += 'A'
    else:
        answer += 'N'
    return answer
