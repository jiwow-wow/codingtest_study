

def dfs(row, sum):
    global min_sum

    if sum >= min_sum:
        return
    if row == N:
        if sum < min_sum:
            min_sum = sum
        return

    for col in range(N):
        if visited[col] == False:
            visited[col] = True
            dfs(row +1, sum + arr[row][col])
            visited[col] = False

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [ list(map(int, input().split())) for _ in range(N) ]

    min_sum = N *10
    visited = [False] * N
    dfs(0,0)
    print(f"#{tc} {min_sum}")