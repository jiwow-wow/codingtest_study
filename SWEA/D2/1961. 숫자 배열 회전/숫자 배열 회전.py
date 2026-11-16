T = int(input())

for tc in range(1, T+1): # 90, 180, 270
    N = int(input())
    l = [input().split() for _ in range(N) ] 
    rev_l = list(zip(*l))
    l_90 =[] 
    l_180 = []
    l_270 =rev_l[::-1]
    
    for row in rev_l:
        l_90.append( list(row[::-1]) )
    for row in l:
        l_180.append( list(row[::-1]))
    l_180 = l_180[::-1]
    
    print(f"#{tc}")
    for i in range(N):
        print(f"{''.join(l_90[i])} {''.join(l_180[i])} {''.join(l_270[i])}")