def solution(answers):
    dic = { "1":0, "2":0, "3":0}
    
    supo1 = [1,2,3,4,5]
    supo2 = [2,1,2,3,2,4,2,5]
    supo3 = [3,3,1,1,2,2,4,4,5,5]
    
    for i, a in enumerate(answers):
        if a ==supo1[ i %len(supo1)] :
            dic["1"] += 1
        if a == supo2[i % len(supo2)]:
            dic["2"] += 1
        if a == supo3[i % len(supo3)]:
            dic["3"] += 1
            
    max_val = max(dic.values() )
    
    return [int(k) for k, v in dic.items() if v == max_val ]

"""
리스트가 더 간편함
score = [0,0,0]


    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result
"""