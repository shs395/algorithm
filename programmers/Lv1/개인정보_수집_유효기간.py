def ymd_to_day(y, m, d):
    return int(d) + (28 * int(m)) + (28 * 12 * int(y))

def solution(today, terms, privacies):
    answer = []
    y, m, d = today.split('.')
    today = ymd_to_day(y, m, d)
    
    term_dict = dict()
    for term in terms:
        a, b = term.split()
        term_dict[a] = b
        
    for idx, privacy in enumerate(privacies):
        ymd, t = privacy.split()
        y, m, d = ymd.split('.')
        
        if today - ymd_to_day(y, m, d) > ymd_to_day(0, term_dict[t], 0) - 1:
            answer.append(idx + 1)
        
    return answer
