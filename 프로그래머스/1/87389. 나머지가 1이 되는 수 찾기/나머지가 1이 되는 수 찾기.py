def solution(n):
    return min([i for i in range(1,n+1) if n%i==1 ])
    # return [x for x in range(1,n+1) if n%x==1][0] #[0]으로 최솟값 접근

#     for i in range(1, n+1):
#         if n%i==1:
#             return i
    
