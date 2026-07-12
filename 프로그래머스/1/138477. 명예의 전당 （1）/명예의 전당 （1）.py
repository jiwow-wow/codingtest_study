def solution(k, score):
    champion = []
    answer = []
    
    for s in score:
        champion.append(s)
        champion = sorted(champion, reverse =True)[:k]
        
        answer.append(min(champion))
    return answer 