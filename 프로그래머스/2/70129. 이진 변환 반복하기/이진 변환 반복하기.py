def solution(s):
    answer = [1,0]
    
    m = ''
    for c in s:
        if c == '0':
            answer[1] +=1
        else:
            m += c
    temp = bin(len(m))[2:]
            
    while (temp != '1'):
        a =''
        for c in temp:
            if c == '0':
                answer[1] += 1
            else:
                a += c
        temp = bin(len(a))[2:]
        answer[0] += 1
        
    return answer