T = int(input())
def arr_sum(A, B):
    s = 0
    for i in range(len(A)):
        pro = A[i]*B[i]
        s += pro
    return s
        
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    #print(A, B)
    if len(A) > len(B):
        B, A = A, B
    
    #0 삽입 횟수 = abs(len(A)- len(B))
    t = len(B) - len(A)
    res= [ ] 
    
    if t == 0: # 길이가 같음
        res.append(arr_sum(A,B))
    
    else:
        res.append(arr_sum(A,B))
        for _ in range(t):
            A.insert(0,0)
            res.append(arr_sum(A,B))
    print(f"#{tc} {max(res)}")