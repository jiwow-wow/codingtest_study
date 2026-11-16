T = int(input())
for tc in range(1, T+1):
    n = float(input())
    
    res = []
    while len(res)<13:# 0~ 12
        n *=2
        
        if n >=1:
            res.append('1')
            n -= 1
        else:
            res.append('0')
        if n ==0:
            break
            
    print(f"#{tc} ", end = "")
    if len(res) < 13:
        print(''.join(res))
    else:
        print("overflow")