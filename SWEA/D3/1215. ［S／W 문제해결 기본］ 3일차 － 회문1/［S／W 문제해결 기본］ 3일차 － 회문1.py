for test_case in range(1,11):
    cnt = 0
    length = int(input())
    arr = [ ]
    for i in range(8):
        arr.append(input() )
    
    for col in arr:
        for i in range(0, 8-length +1):
            s = col[i:i+length]
            if s == s[::-1]:
                cnt +=1
                
    for row in zip(*arr):
        for i in range(0, 8 -length +1):
            s = row[i:i+length]
            if s == s[::-1]:
                cnt += 1
                
    print(f"#{test_case} {cnt}")
    
                