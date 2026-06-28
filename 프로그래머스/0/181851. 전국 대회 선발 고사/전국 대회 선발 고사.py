def solution(rank, attendance):
    dic = {}
    
    for i, r in enumerate(rank):
        if attendance[i]:
            dic[i] = r
    
    soted_dic = dict(sorted(dic.items(), key=lambda x: x[1]))
    arr = list(soted_dic.keys())
    
    return arr[0] * 10000 + arr[1]*100 + arr[2]

'''
리스트컴프리핸션까지는 생각했으나, set을 써서 넣는 방법을 생각하지 못함, 2중 리스트로 시도하다가 실패하였음

def solution(rank, attendance):
    arr = sorted([(x, i) for i, x in enumerate(rank) if attendance[i]])
    return arr[0][1] * 10000 + arr[1][1] * 100 + arr[2][1]
'''