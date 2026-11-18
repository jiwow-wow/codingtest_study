def sq(n):

    if n ==1:
        return 1
    elif n == 2:
        return 3
    elif n > 2:
        if n in memo:
            return memo[n]
        else:
            memo[n] = sq(n-1) + sq(n-2)*2
            return memo[n]


# 30 > 2, 40> 3, 50 >4
T = int(input())

for tc in range(1, T +1):
    N = int(input())
    n = int(N/10)
    memo = {}
    print(f"#{tc} {sq(n)}")


