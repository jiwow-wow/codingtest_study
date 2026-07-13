def solution(name, yearning, photo):
    answer = []
        
    for ps in photo:
        
        sum_y = 0
        for p in ps:
            if p in name:
                sum_y +=yearning [ name.index(p) ]
        answer.append(sum_y)
    
    
    return answer