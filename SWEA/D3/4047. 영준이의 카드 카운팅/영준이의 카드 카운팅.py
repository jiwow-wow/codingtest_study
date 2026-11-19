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
# SWEA 1216: 풀긴함,어려움 회문2 (격자 탐색 / 완전탐색)
# SWEA 1220: 굿 Magnetic (2차원 배열 시뮬레이션)
# SWEA 1289: 음굿? 원재의 메모리 복구하기 (배열 상태 변화 / 시뮬레이션)
# SWEA 2805: 굿 농작물 수확하기 (2차원 배열 규칙 탐색 / 구간 합)
# SWEA 5215: 어려웠음(dfs 안 익숙함) 햄버거 다이어트
# SWEA 5356: 굿 의석이의 세로로 말해요
# SWEA 6485: 굿삼성시의 버스 노선
# SWEA 3499: 굿 D3

# SWEA 4047: D3
# SWEA 5658: 모의 SW 역량테스트
# SWEA 6190: D3
# SWEA 11315: D3
#---------------------------------------------------------



def card(string):

    for i in range((len(string)//3)): # 0123
        al = string[i*3]
        num = int(string[i*3+1:i*3+3]) -1

        if al =="S":
            if l[0][num] == 1:
                return "ERROR"
            else:
                l[0][num] +=1
        elif al =="D":
            if l[1][num] == 1:
                return "ERROR"
            else:
                l[1][num] +=1
        elif al =="H":
            if l[2][num] == 1:
                return "ERROR"
            else:
                l[2][num] +=1
        elif al =="C":
            if l[3][num] == 1:
                return "ERROR"
            else:
                l[3][num] +=1

    sum_list = []
    for i in range(4):
        sum_list.append(13 - sum(l[i]))
    return sum_list



T = int(input())
for tc in range(1,T+1):

    string = input()
    l = [[0]*13 for _ in range(4)]

    res = card(string)
    if res == "ERROR":
        print(f"#{tc} {res}")

    else:
        print(f"#{tc} {' '.join(map(str, res))}")
