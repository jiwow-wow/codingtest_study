def solution(s):
    answer = []
    seen = {}
    
    
    for i,c in enumerate(s):
        if c in seen:
            answer.append( i- seen[c])
        else:
            answer.append(-1)
        seen[c] = i  
    return answer


"""
str.find(char, i ) => str에서 i번째 이후에 등장하는 char의 index를 반환

return [s[i::-1].find(s[i],1) for i in range(len(s))]
"""