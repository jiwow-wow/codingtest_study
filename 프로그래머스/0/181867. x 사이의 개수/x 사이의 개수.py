def solution(myString):
    answer = []
    
    
    answer.extend(myString.split('x'))
    length=list(map(len, answer))
    # length=list(map(lambda x: len(x), answer))
    
    return length

#좋은 풀이(리스트 컴프리헨션 사용): return [len(w) for w in myString.split('x')]