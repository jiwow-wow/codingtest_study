def solution(arr, k):
    answer = []
    
    for n in arr:
        if len(answer) >=k:
            break
        else:
            if n not in answer:
                answer.append(n)
    while len(answer) !=k:
        answer.append(-1)

    return answer 