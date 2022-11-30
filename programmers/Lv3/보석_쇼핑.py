def solution(gems):
    answer = [0, len(gems) + 2]
    gem_dict = dict()
    len_gem_set = len(set(gems))
    end = 0
    for start in range(len(gems)):
        while len(gem_dict) != len_gem_set and end < len(gems):
            if gems[end] not in gem_dict:
                gem_dict[gems[end]] = 1
            else:
                gem_dict[gems[end]] += 1
            end += 1
        
        if len(gem_dict) == len_gem_set and end - (start + 1) < answer[1] - answer[0]:
            answer = [start + 1, end]
            
        if gem_dict[gems[start]] == 1:
            del gem_dict[gems[start]]
        else:
            gem_dict[gems[start]] -= 1
        
    return answer
