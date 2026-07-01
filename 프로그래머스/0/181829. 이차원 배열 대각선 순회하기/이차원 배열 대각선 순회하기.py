def solution(board, k):
    answer = 0
    
    for i,b in enumerate(board):
        for j,b2 in enumerate(b):
            if (i+j) <=k:
                answer += board[i][j]
        
    return answer