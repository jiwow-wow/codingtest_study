# SWEA 4835: D2 이지
# SWEA 5097: D2 이지
# SWEA 1961: D2 굿
# SWEA 1954: D2 방향전환 어려움 - 다시 풀기
# SWEA 2001: D2
# SWEA 1225: D3
# SWEA 1979: D2
# SWEA 1206: D3

def check_pal(s):
    if s == s[::-1]:
        return 1
    return 0

T = int(input())
for tc in range(1, T +1):
    # N = int(input())
    s = input()

    print(f"#{tc}", end= " ")

    if check_pal(s) and  check_pal(s[0:int((len(s)-1)/2)]):
        print("YES")
    else:
        print("NO")

