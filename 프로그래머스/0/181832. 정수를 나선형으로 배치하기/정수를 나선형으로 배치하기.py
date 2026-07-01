def solution(n):
    answer = [[0] * n for _ in range(n)]
    
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    
    r, c = 0, 0
    dir_idx = 0
    
    for num in range(1, n * n + 1):
        answer[r][c] = num
        
        nr = r + dr[dir_idx]
        nc = c + dc[dir_idx]
        
        if nr < 0 or nr >= n or nc < 0 or nc >= n or answer[nr][nc] != 0:
            dir_idx = (dir_idx + 1) % 4  # 0 -> 1 -> 2 -> 3 -> 0 순환
            nr = r + dr[dir_idx]
            nc = c + dc[dir_idx]
        r, c = nr, nc
        
    return answer


'''
기초 중 제일 어려운 문제였음, gpt의 도움을 받음
'''