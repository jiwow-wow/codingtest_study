def solution(x):
    
    answer = [int(n) for n in str(x) ]
    
    if x % sum(answer) ==0:
        return True
    else:
        return False
    
