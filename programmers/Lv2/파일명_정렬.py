def solution(files):
    answer = []
    data = []
    
    for file in files:
        head = ''
        number = ''
        tail = ''
        for i in range(len(file)):
            if ((file[i].isalpha() == True or file[i] == ' ' or  file[i] == '.' or file[i] == '-') and len(number) >= 1) or len(number) > 5:
                tail += file[i:]
                break
            elif file[i].isdigit() == True:
                number += file[i]
            else:
                head += file[i]
        data.append([head, number, tail])
        
    data = sorted(data, key=lambda x:(x[0].lower(), int(x[1])))
    for i in data:
        answer.append(i[0] + i[1] + i[2])
    return answer
