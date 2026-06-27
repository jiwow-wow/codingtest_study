def solution(strArr):
    answer = []#1 2 1 3 2
    arr = []
    
    for s in strArr:
        answer.append(len(s))
        
    for i in set(answer):
        arr.append(answer.count(i))
        
    return max(arr)


'''
딕셔너리 사용
def solution(strArr):
    d = {}

    for i in strArr:
        d[len(i)] = d.get(len(i), 0) + 1

    return max(d.values())
'''