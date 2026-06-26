def solution(arr):
    answer = []
    
    for i in arr:
        for s in range(i):
            answer.append(i)
    
    return answer