def palindrome_8(arr, length):
    arr = arr
    cnt = 0
    length = length
    
    for row in arr: #8번
        p_list = [ ]
        for i in range(0, 8 - length+1):
            p_list = row[i: i+length]
            if check_palidrome(p_list, length):
                cnt +=1
    return cnt

def check_palidrome(p_list, length):
    is_p = True
    p_list = p_list
    length =length
    
    for i in range(length // 2):
        if p_list[i] != p_list[-1-i]:
            is_p = False
            break
    return is_p
    

for test_case in range(1,11):
    total_cnt = 0 
    length = int(input())
    
    arr = [ list(input().strip()) for _ in range(8) ]
    total_cnt += palindrome_8(arr, length)
    
    arr2 = [ list(col) for col in zip(*arr) ]
    total_cnt += palindrome_8(arr2, length)
    
    print(f"#{test_case} {total_cnt}")