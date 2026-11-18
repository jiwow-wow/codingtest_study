# SWEA 4835: D2 이지
# SWEA 5097: D2 이지
# SWEA 1961: D2
# SWEA 1954: D2
# SWEA 2001: D2
# SWEA 1225: D3
# SWEA 1979: D2
# SWEA 1206: D3

def rotate_90(l):
    #0,0 > 0,2   1,0 0,
    #0,1 > 1,2
    #0,2 > 2,2
    new_l = [[0] *N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            new_l[j][N-1-i] =l[i][j]
    return new_l


T = int(input())
for tc in range(1, T +1):

    # N, M = map(int, input().split())
    N = int(input())
    l = [ list(input().split()) for _ in range(N)]

    # rev = list(zip(*l))

    l_90 = rotate_90(l)
    l_180 = rotate_90(l_90)
    l_270 = rotate_90(l_180)
    print(f"#{tc}")

    for i in range(N):
        print(f"{''.join(l_90[i])} {''.join(l_180[i])} {''.join(l_270[i])}")