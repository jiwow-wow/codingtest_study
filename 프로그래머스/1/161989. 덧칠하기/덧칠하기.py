def solution(n, m, section):
    answer = 0
    wall_arr = [True] *n
    
    for s in section:
        wall_arr[s-1] = False
    
    for i in range(n):
        if wall_arr[i] == False:
            for k in range(i, min(i+m, n)):
                wall_arr[k] = True
            answer += 1
    
    
    return answer
"""
def solution(n, m, section):
    answer = 0
    painted = 0

    for s in section:
        if s > painted:
            answer += 1
            painted = s + m - 1

    return answer

"""
