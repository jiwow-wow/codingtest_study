def solution(n):
    
    answer=[[0] *n for _ in range(n) ]  
    
    for i in range(n):
        answer[i][i] = 1
    
    
    return answer

"""
이중 for문 없이 [i][i]로 해결
"""