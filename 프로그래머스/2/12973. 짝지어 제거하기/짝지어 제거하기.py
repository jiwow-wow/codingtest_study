def solution(s):
    answer = 1
    l = []
    
    for c in s:        
        if len(l) !=0 and l[-1] == c:
            l.pop()
        
        else:
            l.append(c)
    if len(l) != 0:
        answer = 0
    
    
    return answer