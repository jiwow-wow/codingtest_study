def solution(arr, k):
    answer = []
    
    
    
    
    if k%2==0:
        answer = list(map(lambda x: x+k, arr))
    else:
        answer = list(map(lambda x: x*k , arr))
            
    return answer 

"""
return [i*k if k%2!=0 else i+k for i in arr]
"""