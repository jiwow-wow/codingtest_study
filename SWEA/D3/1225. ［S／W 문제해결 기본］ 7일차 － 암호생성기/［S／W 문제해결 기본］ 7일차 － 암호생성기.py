for test_case in range(1,11):
    _  = input()
    code = list(map( int, input().split())) 
    #print(code)
    #print(code.pop())
    is_break = False
    
    while(not is_break):
        for i in range(1,6):
            new_c = code[0] - i
            
            if new_c <= 0:
                new_c =0
                is_break = True
                code.pop(0)
                code.append(new_c)
                break
            code.pop(0)
            code.append(new_c)
    result = " ".join(map(str , code))
    print(f"#{test_case} {result}")