def solution(arr):
    answer = 1
    
    for i,n in enumerate(arr):
        for j in range(len(n)):
            if arr[i][j] == arr[j][i]:
                continue
            else:
                return 0 
                
    return answer

