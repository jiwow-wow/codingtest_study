T = int(input())

for tc in range(1,T+1):
    x, y, N = map(int, input().split())
    
    cnt = 0
    while( x <= N or y <= N):
        # 1,100   [101, 100] [1, 101]   [201, 100] [101, 201]
        if max(x,y) +min(x,y) >N:
            cnt +=1 
            break
        
        if  x < y:
            x += y
        else:
            y += x
        cnt += 1
    print(cnt)