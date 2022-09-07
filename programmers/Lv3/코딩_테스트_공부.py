def solution(alp, cop, problems):
    answer = 0
    max_alp = alp
    max_cop = cop
    for i in problems:
        if i[0] > max_alp:
            max_alp = i[0]
        if i[1] > max_cop:
            max_cop = i[1]
    print(alp, cop)
    print(max_alp, max_cop)
    data = [[151 for _ in range(max_cop + 1)] for _ in range(max_alp + 1)]
    data[alp][cop] = 0
    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):
            if i + 1 <= max_alp:
                data[i + 1][j] = min(data[i][j] + 1, data[i + 1][j])
            if j + 1 <= max_cop:
                data[i][j + 1] = min(data[i][j] + 1, data[i][j + 1])
            for problem in problems:
                if problem[0] <= i and problem[1] <= j:
                    if i + problem[2] >= max_alp and j + problem[3] >= max_cop:
                        data[max_alp][max_cop] = min(data[max_alp][max_cop], data[i][j] + problem[4])
                    elif i + problem[2] >= max_alp:
                        data[max_alp][j + problem[3]] = min(data[max_alp][j + problem[3]], data[i][j] + problem[4])
                    elif j + problem[3] >= max_cop:
                        data[i + problem[2]][max_cop] = min(data[i + problem[2]][max_cop], data[i][j] + problem[4])
                    elif i + problem[2] < max_alp and j + problem[3] < max_cop:
                        data[i + problem[2]][j + problem[3]] = min(data[i + problem[2]][j + problem[3]], data[i][j] + problem[4])
    return data[max_alp][max_cop]
