# 우선 진출 지점을 기준으로 정렬한다..
# 그리고 거기에 카메라를 세움
# 그리고 다음 것부터 진입 지점을 기준으로 비교
# 새로운 진출 지점은 앞의 진출 지점보다 뒤거나 같으므로
# 진입 지점이 앞의 진출 지점의 뒤냐 앞이냐로 나눌 수 있음
# 뒤면 안만남 앞이면 만남(카메라 재설정 x)
def solution(routes):
    answer = 0
    camera = -30001
    routes.sort(key=lambda x:x[1])
    for route in routes:
        if camera < route[0]:
            answer += 1
            camera = route[1]
    return answer
