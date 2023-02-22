def time_to_ms(s):
    h, m, s_ms = s.split(':')
    return int(h) * 60 * 60 * 1000 + int(m) * 60 * 1000 + int(float(s_ms) * 1000)

def solution(lines):
    answer = 0
    data = []
    for line in lines:
        a, b, c = line.split()
        end = time_to_ms(b)
        start = end - int(float(c[:-1]) * 1000) + 1
        if start < 0:
            start = 0
        data.append((start, end))
    
    for x in data:
        for i in range(2):
            cnt = 0
            for y in data:
                if y[1] >= x[i] and y[0] < x[i] + 1000:
                    cnt += 1
            answer = max(answer, cnt)
    
    return answer
