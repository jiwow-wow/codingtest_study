def solution(arr):
    answer = [[]]
    
    x = len(arr)
    y = len(arr[0])
    
    if x > y:
        for i,n in enumerate(arr):
            arr[i].extend( [0]*(x-y))
            
    elif x < y:
        for _ in range(y-x):
            arr.append([0]*y)
    return arr