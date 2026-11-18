# SWEA 4835: D2 이지
# SWEA 5097: D2 이지
# SWEA 1961: D2 굿
# SWEA 1954: D2 방향전환 어려움 - 다시 풀기(2회차 맞음)
# SWEA 2001: D2 파리퇴치 어려움 - 다시풀기(2회차 맞음)
# SWEA 20019: D3 이지 회문 판별
# SWEA 1225: D3 이지
# SWEA 1979: D2
# SWEA 1206: D3



T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    l = [ list(map(int, input().split())) for _ in range(N) ]
    # print(l)

    rev = [ list(row) for row in zip(*l) ]
    cnt =0

    for row in l:
        for i in range(N-K+1): #0~2
            if row[i:i+K] == [1]*K:
                if i == 0: #처음일 때, 뒤에 1개만 확인
                    if row[i+K] == 0:
                        cnt += 1
                elif 1 <= i <= N-K-1: #중간일 떄 앞에 뒤에 확인
                    if row[i-1] ==0 and row[i+K] ==0 :
                        cnt += 1
                elif i == N-K: # 마지막일 때 앞에 하나만 확인
                    if row[i-1] == 0:
                        cnt +=1

    for row in rev:
        for i in range(N - K + 1):  # 0~2
            if row[i:i + K] == [1] *K:
                if i == 0:  # 처음일 때, 뒤에 1개만 확인
                    if row[i + K] == 0:
                        cnt += 1
                elif 1 <= i <= N - K - 1:  # 중간일 떄 앞에 뒤에 확인
                    if row[i - 1] == 0 and row[i + K] == 0:
                        cnt += 1
                elif i == N - K:  # 마지막일 때 앞에 하나만 확인
                    if row[i - 1] == 0:
                        cnt += 1

    print(f"#{tc} {cnt}")