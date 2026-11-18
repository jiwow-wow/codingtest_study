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
# SWEA 1209: 이지 Sum (2차원 배열 구간 합 / 완전탐색)
# SWEA 1215: 이지 회문1 (격자 탐색 / 슬라이딩 구간 검사)
# SWEA 1216: 풀긴함 어려움 회문2 (격자 탐색 / 완전탐색)
# SWEA 1220: Magnetic (2차원 배열 시뮬레이션)
# SWEA 1289: 원재의 메모리 복구하기 (배열 상태 변화 / 시뮬레이션)
# SWEA 2805: 농작물 수확하기 (2차원 배열 규칙 탐색 / 구간 합)
# SWEA 5215: 햄버거 다이어트 (완전탐색 / 조합)
# SWEA 5356: 의석이의 세로로 말해요 (배열 인덱스 조작 / 구현)
# SWEA 6485: 삼성시의 버스 노선 (범위 카운팅 / 완전탐색)

for _ in range(10):
    tc = int(input())
    grid = [input().strip() for _ in range(100)]

    max_len = 1

    # 길이가 100부터 1까지 내림차순으로 확인하여 가장 먼저 찾아지는 회문의 길이를 구함
    for length in range(100, 0, -1):
        found = False

        # 1. 가로 검사
        for r in range(100):
            for c in range(100 - length + 1):
                row_str = grid[r][c:c + length]
                if row_str == row_str[::-1]:
                    found = True
                    break
            if found:
                break

        if found:
            max_len = length
            break

        # 2. 세로 검사
        for c in range(100):
            for r in range(100 - length + 1):
                col_str = "".join(grid[r + i][c] for i in range(length))
                if col_str == col_str[::-1]:
                    found = True
                    break
            if found:
                break

        if found:
            max_len = length
            break

    print(f"#{tc} {max_len}")


