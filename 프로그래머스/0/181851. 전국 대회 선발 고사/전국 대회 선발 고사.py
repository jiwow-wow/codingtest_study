def solution(rank, attendance):
    dic = {}
    
    for i, r in enumerate(rank):
        if attendance[i]:
            dic[i] = r
    
    soted_dic = dict(sorted(dic.items(), key=lambda x: x[1]))
    arr = list(soted_dic.keys())
    
    return arr[0] * 10000 + arr[1]*100 + arr[2]