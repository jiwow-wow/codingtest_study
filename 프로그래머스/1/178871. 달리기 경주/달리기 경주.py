def solution(players, callings):
    answer = []
    
    p_dict = { p: i for i, p in enumerate(players)}
    
    for c in callings:
        idx = p_dict[c]
        front_player = players[idx - 1]
        players[idx], players[idx- 1] = players[idx- 1], players[idx]
        
        p_dict[c] = idx - 1
        p_dict[front_player] = idx
        
    return players


# def solution(players, callings):
#     answer = []
    
#     for c in callings:
#         i = players.index(c)
#         players.pop(i)
#         players.insert(i-1, c)
        
#     return players
