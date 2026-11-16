def turn_90(arr, N): #00-> 02, 01->1,0 2,2-> 2,0
    
    res = [ [0]* N for _ in range(N) ] #i0 > jN-1,  i1 > jN-2 i2>jN-3 and j0>iN
    for i in range(N):
        for j in range(N):
            res[j][N-1-i] = arr[i][j]
    return res

T = int(input())
for tc in range(1, T+1): 
    N = int(input())
    l = [input().split() for _ in range(N) ] 
    
    l_90 = turn_90(l, N)
    l_180 = turn_90(l_90, N)
    l_270 = turn_90(l_180, N)

    print(f"#{tc}")
    for i in range(N):
        print(f"{''.join(l_90[i])} {''.join(l_180[i])} {''.join(l_270[i])}")
