def solution(s):
    answer = True
    s_list = []
    
    for c in s:
        if c == "(":
            s_list.append(c)
        elif c == ")":
            if len(s_list) != 0 and s_list[-1] == "(":
                s_list.pop()
            else:
                answer = False
    if len(s_list) != 0:
        answer = False
    
    

    return answer