from collections import deque

T = int(input())

for tc in range(1, T +1):
    N, M = map(int, input().split())
    l = list(map( int, input().split()))
    d = deque(l)
    # print(N, M, l)

    for i in range(M):
        # l.append(l.pop(0))
        d.append(d.popleft())

    print(f"#{tc} {d[0]}")