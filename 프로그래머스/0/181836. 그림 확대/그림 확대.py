def solution(picture, k):
    answer = []
    
    for i,pic in enumerate(picture):
        new_str = ''
        
        for p in pic:
            new_str += p *k
        
        for _ in range(k):
            answer.append(new_str)
        
    return answer

'''
다른 풀이: replace 두번 사용하는 방법도 있음
answer.append(picture[i].replace('.', '.' * k).replace('x', 'x' * k))

'''