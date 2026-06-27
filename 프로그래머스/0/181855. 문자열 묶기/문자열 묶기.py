def solution(strArr):
    answer = []#1 2 1 3 2
    arr = []
    
    for s in strArr:
        answer.append(len(s))
        
    for i in set(answer):
        arr.append(answer.count(i))
        
    return max(arr)