def n_m(n, m): # 9^8 = 9^7 * 9 ... 9^2 = 9^1*9 
    n = n
    m = m
    
    if m == 1:
        return n*m
    else:
        return n_m(n, m-1) * n

for test_case in range(1,11):
    _ = input()
    n, m = input().split()
    n = int(n)
    m = int(m)
    
    print(f"#{test_case} {n_m(n,m)}")