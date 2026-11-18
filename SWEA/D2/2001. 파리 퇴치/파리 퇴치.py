# SWEA 4835: D2 이지
# SWEA 5097: D2 이지
# SWEA 1961: D2 굿
# SWEA 1954: D2 방향전환 어려움 - 다시 풀기(2회차 맞음)
# SWEA 2001: D2 어려움 - 다시풀기(2회차 맞음)
# SWEA 20019: D3 이지 회문 판별
# SWEA 1225: D3 이지
# SWEA 1979: D2
# SWEA 1206: D3



T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    l = [ list(map(int, input().split())) for _ in range(N)]
    # print(l)

    max_n = 0

    for i in range(N-M+1): # 4: 0~3
        for j in range(N-M+1):
            s = 0
            for x in range(i, i+M): #3: 012
                for y in range(j, j+M):
                    s += l[x][y]
            if s > max_n:
                max_n =s

    print(f"#{tc} {max_n}")