def solution(arr, divisor):
    answer = [a for a in arr if (a%divisor==0)]
    
    
    return sorted(answer) or [-1]