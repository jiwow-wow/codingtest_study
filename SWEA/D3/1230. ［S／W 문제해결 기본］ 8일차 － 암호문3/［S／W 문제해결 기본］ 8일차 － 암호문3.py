for tc in range(1,11):
    text_len = int(input())
    text = list(input().split())
    com_len = int(input())
    com = list(input().split())
    
    i =0
    while( i< len(com)):
        if com[i] == "I":
            x = int(com[i+1])
            y = int(com[i+2])
            s = com[i+3:i+3+y]
            text[x:x] = s
            i += 3+y
        elif com[i] == "D":
            x = int(com[i+1])
            y = int(com[i+2])
            
            for _ in range(y):
                text.pop(x)
            i+= 3
        elif com[i] == "A":
            y= int(com[i+1])
            s = com[i+2:i+2+y]
            
            text.extend(s)
            i+= 2 +y
    result = " ".join(map(str, text[0:10]))
    print(f"#{tc} {result}")