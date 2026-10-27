def solution(s):
    answer = [0,0]
    while( s != '1'):
        
        answer[1] += s.count('0')
        temp= "1" * s.count('1')
        s = bin(len(temp))[2:]
        answer[0] += 1
    
    return answer