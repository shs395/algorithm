def make_new_key(key, len_lock):
    len_key = len(key)
    new_key = []
    for j in range(len_lock - 1):
        temp = [0] * (2 * (len_lock - 1) + len_key)
        new_key.append(temp)

    for j in range(len_key):
        temp = [0] * (len_lock - 1)
        temp.extend(key[j])
        temp.extend([0] * (len_lock - 1))
        new_key.append(temp)

    for j in range(len_lock - 1):
        temp = [0] * (2 * (len_lock - 1) + len_key)
        new_key.append(temp)
    return new_key

def rotate_lock(lock):
    rotated_lock = []
    for i in range(len(lock)):
        temp = []
        for j in range(len(lock) - 1, -1, -1):
            temp.append(lock[j][i])
        rotated_lock.append(temp)
        
    return rotated_lock
    
def check_fit(new_key, lock):
    len_lock = len(lock)
    len_new_key = len(new_key)
    for i in range(len_new_key - (len_lock - 1)):
        for j in range(len_new_key - (len_lock - 1)):
            temp_fit = True
            for a in range(len_lock):
                for b in range(len_lock):
                    if lock[a][b] == 0 and new_key[i + a][j + b] == 0:
                        temp_fit = False
                        continue
                    if lock[a][b] == 1 and new_key[i + a][j + b] == 1:
                        temp_fit = False
            
            if temp_fit == True:
                return True
    return False
        
def solution(key, lock):
    answer = False
    new_key = make_new_key(key, len(lock))
    
    for i in range(4):
        if check_fit(new_key, lock) == True:
            return True
        if i < 3:
            lock = rotate_lock(lock)
            
    return answer
