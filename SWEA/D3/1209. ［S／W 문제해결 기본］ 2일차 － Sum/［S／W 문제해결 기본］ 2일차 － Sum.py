# SWEA 4835: D2 이지
# SWEA 5097: D2 이지
# SWEA 1961: D2 굿
# SWEA 1954: D2 방향전환 어려움 - 다시 풀기(2회차 맞음)
# SWEA 2001: D2 파리퇴치 어려움 - 다시풀기(2회차 맞음)
# SWEA 20019: D3 이지 회문 판별
# SWEA 1225: D3 이지
# SWEA 1979: D2 중간(혼자 풀긴함)
# SWEA 1206: D3 이지

# D3
# SWEA 1208: 이지 Flatten (배열 조작 / 최댓값·최솟값 탐색)
# SWEA 1209: Sum (2차원 배열 구간 합 / 완전탐색)
# SWEA 1215: 회문1 (격자 탐색 / 슬라이딩 구간 검사)
# SWEA 1216: 회문2 (격자 탐색 / 완전탐색)
# SWEA 1220: Magnetic (2차원 배열 시뮬레이션)
# SWEA 1289: 원재의 메모리 복구하기 (배열 상태 변화 / 시뮬레이션)
# SWEA 2805: 농작물 수확하기 (2차원 배열 규칙 탐색 / 구간 합)
# SWEA 5215: 햄버거 다이어트 (완전탐색 / 조합)
# SWEA 5356: 의석이의 세로로 말해요 (배열 인덱스 조작 / 구현)
# SWEA 6485: 삼성시의 버스 노선 (범위 카운팅 / 완전탐색)

# T = int(input())
for tc in range(1, 11):
    # N, K = map(int, input().split())
    _ = int(input())
    l = [list(map(int, input().split())) for _ in range(100) ]
    # print(l)

    N = 100
    max_sum = 0
    right_down_sum = 0
    left_down_sum = 0

    for i in range(N):
        row_sum = 0 #i 증가마다 초기화
        col_sum = 0
        right_down_sum += l[i][i]
        left_down_sum += l[i][99-i]

        for j in range(N):
            row_sum += l[i][j]
            col_sum += l[j][i]


        if max(row_sum, col_sum) > max_sum:
            max_sum = max(row_sum, col_sum)
    print(f"#{tc} {max(max_sum,right_down_sum, left_down_sum )}")