def solution(brown, yellow):

    answer = [0,0]
    l = []
    area = brown + yellow
    
    for i in range(2, area//2+1):
        if area % i ==0:
            l.append(i)
            
    for j in range(len(l)):
        for k in range(j, len(l)):
            if (l[j] * l[k] == area) and (l[k]-2) * (l[j]-2) == yellow:
                answer = [l[k], l[j]]
    
    
    
    return answer
            