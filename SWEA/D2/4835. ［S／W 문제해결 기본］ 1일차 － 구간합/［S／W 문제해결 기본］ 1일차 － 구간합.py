T = int(input())

for tc in range(1, T +1):
    N, M = map(int, input().split())
    l = list(map( int, input().split()))
    # print(N, M, l)

    sum_ = []
    for i in range(N-M+1): #5,3 : 0~2
        sum_.append(sum(l[i:i+M]))
    print(f"#{tc} {max(sum_)-min(sum_)}")
