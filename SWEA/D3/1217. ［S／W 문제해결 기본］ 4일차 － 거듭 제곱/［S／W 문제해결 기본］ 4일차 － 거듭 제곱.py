def power(n,m, memo ={}):
    if m == 0:
        return 1
    if m == 1:
        return n
    
    if m in memo:
        return memo[m]
    
    else:
        half = power(n, m//2, memo)
        
        if m % 2 == 0:
            memo[m] = half * half 
        else:
            memo[m] = half * half * n
        return memo[m]

for test_case in range(1,11):
    _ = input()
    n,m = input().split(" ")
    n = int(n)
    m = int(m)
    
    memo = {}
    print(f"#{test_case} {power(n,m, memo)} ")