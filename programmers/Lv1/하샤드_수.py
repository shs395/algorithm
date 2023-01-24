def solution(x):
    if x % sum(map(int, list(str(x)))) == 0:
        return True
    return False
