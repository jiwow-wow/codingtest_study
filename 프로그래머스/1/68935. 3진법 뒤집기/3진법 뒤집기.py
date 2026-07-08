def solution(n):
    answer = ''
    result = 0
    
    while (n !=0):
        answer += str(n % 3)
        n //=3
        
    for i, num in enumerate(answer[::-1]):
        result += int(num)*(3**i)
    
    return result
'''
int() 함수에는 n진수로 만들어주는 기능이 있다
return int(answer, 3)
'''
