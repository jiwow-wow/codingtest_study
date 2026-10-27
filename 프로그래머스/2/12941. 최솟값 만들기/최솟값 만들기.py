def solution(A,B):

    sum = 0
    A.sort()
    B.sort(reverse = True)
    print(A, B)
    for i in range(len(A)):
        sum += A[i] *B[i]
        
#     for i in range(len(A)):
#         min_A = min(A)
#         max_B = max(B)
        
#         A.remove(min_A)
#         B.remove(max_B)
            
#         sum += min_A * max_B
    
    return sum