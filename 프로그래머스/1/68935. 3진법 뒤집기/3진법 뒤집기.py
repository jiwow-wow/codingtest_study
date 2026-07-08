def solution(n):
    answer = ''
    result = 0
    
    while (n !=0):
        answer += str(n % 3)
        n //=3
        
    for i, num in enumerate(answer[::-1]):
        result += int(num)*(3**i)
        

    
    return result