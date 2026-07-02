def solution(n):
    answer = []
    
    # n//2 를 하면 성능 약 2배 향상 
    for i in range(1, n//2+1):
        if n%i ==0:
            answer.append(i)
    
    return sum(answer)+n
    # return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])