def solution(board, moves):
    answer = []
    result =0

    for m in moves:
        for i, b in enumerate(board):
            if b[m-1] != 0:
                answer.append(b[m-1])
                
                if len(answer) >= 2 and answer[-1] == answer[-2]:
                    result +=2
                    for k in range(2):
                        answer.pop()
                
                board[i][m-1] = 0
                break
    
    
    return result