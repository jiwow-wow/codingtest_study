def solution(picture, k):
    answer = []
    
    for i,pic in enumerate(picture):
        new_str = ''
        
        for p in pic:
            new_str += p *k
        
        for _ in range(k):
            answer.append(new_str)
        
    return answer