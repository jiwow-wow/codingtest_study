# SWEA 4835: D2 이지
# SWEA 5097: D2 이지
# SWEA 1961: D2 굿
# SWEA 1954: D2 방향전환 어려움 - 다시 풀기
# SWEA 2001: D2 어려움 - 다시풀기
# SWEA 20019: D3 이지 회문 판별
# SWEA 1225: D3
# SWEA 1979: D2
# SWEA 1206: D3



# T = int(input())
for tc in range(1, 11):
    # N, M= map(int, input().split())
    _ = int(input())
    l = list(map(int, input().split()))
    # print(l)

    w_b = False

    while True:
        for i in range(1,6):
            num = l.pop(0) - i
            l.append(num)
            if num <= 0:
                l[-1] = 0
                w_b = True
                break

        if w_b:
            break
    l = map(str, l)
    print(f"#{tc} {' '.join(l)}")