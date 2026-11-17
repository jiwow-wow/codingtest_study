T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    l = list(map(int, input().split()))

    for _ in range(M):
        l.append(l.pop(0))
    print(f"#{tc} {l[0]}")