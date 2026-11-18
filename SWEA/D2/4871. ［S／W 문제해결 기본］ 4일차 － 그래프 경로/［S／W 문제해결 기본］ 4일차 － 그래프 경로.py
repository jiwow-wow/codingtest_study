

def dfs(s, g):
    if s ==g:
        return 1
    visited[s] =True

    for n in node[s]:
        if visited[n] == False:
            if dfs(n,g) == 1:
                return 1
    return 0

T = int(input())

for tc in range(1, T +1):
    V, E = map(int, input().split())

    node = [[] for _ in range (V+1)]
    visited = [False] * (V+1)

    for _ in range(E):
        a, b = map(int, input().split())
        node[a].append(b)


    s,g = map(int, input() .split())
    print(f"#{tc} {dfs(s, g)}")