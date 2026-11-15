
for tc in range(1,11): 
    text_l = int(input())
    text = list(map(str, input().split()))
    com_l = int(input())
    command = list(input().split())
    
    i = 0
    while( i < len(command) ):
        if command[i] == 'I':
            x = int(command[i+1])
            y = int(command[i+2])
            s = command[i+3: i+3+y]
            text[x:x] = s
            #print(text)
            i = i+3+y
            
        elif command[i] == 'D':
            x = int(command[i+1])
            y = int(command[i+2])
            for _ in range(y):
                text.pop(x)
            i = i+3
    result = " ".join(map(str, text[0:10]))
    print(f"#{tc} {result}")