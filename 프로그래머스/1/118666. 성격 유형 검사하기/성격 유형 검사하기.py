def solution(survey, choices):
    answer = ''
    p_dict = {'R':0 , 'T':0, 'C':0, 'F':0 ,'J':0, 'M':0, 'A':0, 'N':0}
    # p_dict = {'RT':0 , 'CF':0, 'JM':0, 'AN':0}

    
    for i, c in enumerate(choices):
        if c < 4 : 
            p_dict[survey[i][0]] += 4-c
        elif c > 4: 
            p_dict[survey[i][1]] += c-4

    indicaters = [['R', 'T'], ['C', 'F'], ['J', 'M'], ['A', 'N']]
    
    for t1, t2 in indicaters:
        if p_dict[t1] >= p_dict[t2]:
            answer += t1
        else:
            answer += t2

    return answer