for test_case in range(1,11):
    _ = input()
    arr = [ list(map(int, input().split())) for x in range(100)]
    
    
    #max_row = max( sum(row) for row in arr )
    max_row =0
    for row in arr:
        if max_row <= sum(row):
            max_row = sum(row)
            
    max_col = 0 
    for col in zip(*arr):
        sum_col = sum(col)
        if max_col <= sum_col:
            max_col = sum_col
            
    right_down =0
    left_down =0
    for i in range(100):
        right_down += arr[i][i]
        left_down +=arr[i][99-i]
        
    print(f"#{test_case} {max(max_row, max_col, right_down, left_down)}")
        