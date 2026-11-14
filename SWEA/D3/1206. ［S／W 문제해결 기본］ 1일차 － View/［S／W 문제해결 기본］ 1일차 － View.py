def building_view(b_list):
    answer = [] 
    
    for i, b  in enumerate(b_list):
        if b == 0 or i in (0,1,len(b_list)-2,len(b_list)-1):
            answer.append(0)
            continue
            
        max_h = max(b_list[i-2], b_list[i-1], b_list[i+1], b_list[i+2] )
        if max_h > b:
            answer.append(0)
        elif b > max_h:
            answer.append(b - max_h)
    return answer

for test_case in range(1,11):
    b_num = input()
    b_list = list(map(int, input().split() ))
    view_sum = sum( building_view(b_list) )
    print(f"#{test_case} {view_sum}")
    

    
    