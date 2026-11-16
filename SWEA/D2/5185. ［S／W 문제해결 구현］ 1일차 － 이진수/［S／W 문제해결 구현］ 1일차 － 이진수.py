T = int(input())

ox_l = [ str(x) for x in range(10) ]
ox_l.extend(["A", "B", "C", "D", "E", "F"])
ox_dic = {} 
for i,x in enumerate(ox_l):
    ox_dic[x] = i
    
for t in range(1,T+1):
    N, X = input().split(" " )
    res = ""
    
    for x in X:
        temp = bin(ox_dic[x])[2::]
        if len(temp) <4:
            res += '0'* (4- len(temp))
        res += temp
        
    print(f"#{t} {res}")