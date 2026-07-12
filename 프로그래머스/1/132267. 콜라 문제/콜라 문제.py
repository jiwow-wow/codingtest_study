def solution(a,b,n):
    total =0
    
    while( n//a >0):
        sub = n%a
        n = (n//a) *b
        total += n
        n+=sub        
    
    return total
"""
    while n >= a:
        answer += (n // a) * b
        n = (n // a) * b + (n % a)
"""
