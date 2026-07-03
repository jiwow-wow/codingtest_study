def solution(n): #재귀함수로 제작
    
    if n >= 10:
        return n%10 + solution(n//10)
    
    else:
        return n%10
    
    


# def solution(n):
#     answer =0
    
#     for num in str(n):
#         answer += int(num)

#     return answer