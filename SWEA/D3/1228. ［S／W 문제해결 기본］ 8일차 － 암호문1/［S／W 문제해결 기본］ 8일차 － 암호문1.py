for test_case in range(1,11):
    text_len = int(input())
    text= list(map(int, input().split() ))
    com_len = int(input())
    command = list(input().split())
    
    i =0
    while i < len(command):
        if command[i] == "I":
            x = int(command[i+1])
            y = int(command[i+2])
            s = command[i+3: i+3+y]
            
            text[x:x] = s 
            i += 3+y
    result = " ".join(map(str, text[0:10]))
    print(f"#{test_case} {result}")