T = int(input())

for tc in range(1,T+1):
    N = int(input())
    l = [ list(map(int, input())) for _ in range(N)]
    # print(l)

    total =0
    mid = N//2
    n=0
    for idx, row in enumerate(l):

        if idx <= mid:
            n += 1
        elif idx > mid:
            n -= 1
        total += sum(row[mid-n+1:mid+n])
    print(f"#{tc} {total}")

