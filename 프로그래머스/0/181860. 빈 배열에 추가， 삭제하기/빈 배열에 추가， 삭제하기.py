def solution(arr, flag):
    answer = []
    
    for i,b in enumerate(flag):
        if b:
            for _ in range(arr[i]*2):
                answer.append(arr[i])
        else:
            for _ in range(arr[i]):
                answer.pop()
        # print(answer)
    return answer