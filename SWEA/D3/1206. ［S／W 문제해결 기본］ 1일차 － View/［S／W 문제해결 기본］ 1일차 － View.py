# SWEA 4835: D2 이지
# SWEA 5097: D2 이지
# SWEA 1961: D2 굿
# SWEA 1954: D2 방향전환 어려움 - 다시 풀기(2회차 맞음)
# SWEA 2001: D2 파리퇴치 어려움 - 다시풀기(2회차 맞음)
# SWEA 20019: D3 이지 회문 판별
# SWEA 1225: D3 이지
# SWEA 1979: D2 중간(혼자 풀긴함)
# SWEA 1206: D3


# T = int(input())
for tc in range(1, 11):
    # N, K = map(int, input().split())
    N = int(input())
    l = list(map(int, input().split(" ")))
    cnt = 0

    for i in range(2, N-3+1): # 2~7
        if  l[i] == 0:
            continue

        max_ = max([l[i-2], l[i-1], l[i+1], l[i+2]])
        if max_ <l[i]:
            cnt += l[i] - max_




    print(f"#{tc} {cnt}")