# SWEA 4835: D2 이지
# SWEA 5097: D2 이지
# SWEA 1961: D2 굿
# SWEA 1954: D2 방향전환 어려움 - 다시 풀기(2회차 맞음)
# SWEA 2001: D2 어려움 - 다시풀기(
# SWEA 20019: D3 이지 회문 판별
# SWEA 1225: D3 이지
# SWEA 1979: D2
# SWEA 1206: D3



T = int(input())
for tc in range(1, T+1):
    N = int(input())

    l = [ [0]*N for _ in range(N)]

    # 방향 우 하 좌 상
    dir_r = [0,1,0,-1]
    dir_c = [1,0,-1,0]

    idx = 0
    r, c =0, 0
    for i in range(1, N*N+1): # 1~N*N
        l[r][c] = str(i)

        nex_r = r + dir_r[idx]
        nex_c = c + dir_c[idx]

        if not(0 <= nex_r <= N-1 and 0 <=nex_c <= N-1) or l[nex_r][nex_c] != 0: #범위 탈출 or 다음에 값이 있음

            #방향 전환
            idx = (idx +1)%4
            nex_r = r + dir_r[idx]
            nex_c = c + dir_c[idx]

        r = nex_r
        c = nex_c

    print(f"#{tc}")
    for n in range(N):
        # print(l[n])
        print(' '.join(l[n]))


