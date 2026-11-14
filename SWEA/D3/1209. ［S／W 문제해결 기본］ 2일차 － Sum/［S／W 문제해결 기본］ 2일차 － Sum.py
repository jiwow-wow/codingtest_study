for test_case in range(1,11):
    _ = input()
    
    arr_list = [0] *100
    for i in range(100):
        arr_list[i] = list(map(int, input().split() ))
        
    sum_list = [0] *202
    for i in range(100):
        sum_list[i] = sum(arr_list[i])  # 0~99:  arr_list 열의 합
        sum_list[200] += arr_list[-i][-i] #우상향 대각
        sum_list[201] += arr_list[i][i]
        for j in range(100):
            sum_list[100+i] += arr_list[j][i] # 100 ~199: 행의 합
                
    print(f"#{test_case} {max(sum_list)}")