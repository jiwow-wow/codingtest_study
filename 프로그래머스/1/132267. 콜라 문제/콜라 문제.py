def solution(a, b, n):
    answer = cola_return(a, b, n)
    return answer

def cola_return(a,b,n):
    total =0
    
    while( n//a >0):
        sub = n%a
        n = (n//a) *b
        total += n
        n+=sub
            
        print(n, total, sub)
        
    
    return total