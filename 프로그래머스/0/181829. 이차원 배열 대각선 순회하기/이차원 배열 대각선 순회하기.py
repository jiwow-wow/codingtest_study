def solution(board, k):
    answer = 0
    
    for i,b in enumerate(board):
        # print(i)
        for j,b2 in enumerate(b):
            # print(i, j)
            if (i+j) <=k:
                # print(i, j)
                answer += board[i][j]
        
    return answer