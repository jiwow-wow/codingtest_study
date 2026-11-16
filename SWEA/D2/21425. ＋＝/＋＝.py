T = int(input())

for tc in range(1,T+1):
    x, y, N = map(int, input().split())
    
    cnt = 0
    while(x<=N or y<=N):
        if x < y:
            x += y
        else:
            y +=x
        cnt +=1
    
    print(cnt-1)