for tc in range(1,11):
    n, code = input().split(" ")
    n = int(n)
    c_list = list(code)
    
    i= 0
    while i < len(c_list)-1:
        if c_list[i] ==c_list[i+1]:
            c_list.pop(i)
            c_list.pop(i)
            i -= 1
            
        else:
            i += 1
    result = "".join(c_list)
    print(f"#{tc} {result}")
    
    