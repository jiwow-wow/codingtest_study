# SWEA 4835: D2 이지
# SWEA 5097: D2 이지
# SWEA 1961: D2
# SWEA 1954: D2
# SWEA 2001: D2
# SWEA 1225: D3
# SWEA 1979: D2
# SWEA 1206: D3

T = int(input())

for tc in range(1, T +1):

    # N, M = map(int, input().split())
    N = int(input())
    l = [ list(input().split()) for _ in range(N)]

    rev = list(zip(*l))

    l_90 = [ row[::-1] for row in rev ]
    l_180 = [ row[::-1] for row in l][::-1]
    l_270 = [ row for row in rev][::-1]
    print(f"#{tc}")

    for i in range(N):
        print(f"{''.join(l_90[i])} {''.join(l_180[i])} {''.join(l_270[i])}")