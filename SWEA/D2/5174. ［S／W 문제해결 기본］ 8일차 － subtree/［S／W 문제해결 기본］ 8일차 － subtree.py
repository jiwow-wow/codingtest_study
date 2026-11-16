
T = int(input())
for tc in range(1,T+1):
    E, N = map(int, input().split())
    l = list(map(int, input().split()))

    left = [0] * (E+2)
    right = [0] * (E+2)

    for i in range(0, len(l), 2):
        p = l[i]
        c = l[i+1]

        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c


    def cntnode(n):
        if n ==0:
            return 0
        return 1 + cntnode(left[n]) + cntnode(right[n])
    print(f"#{tc} {cntnode(N)}")