T = int(input())
for tc in range(1,T+1):
    P, Q, R, S, W= map(int, input().split(" "))

    A_comp = P * W

    if W <= R:
        B_comp = Q
    else:
        over = W-R
        B_comp = over * S + Q

    print(f"#{tc} {min(A_comp, B_comp)}")

