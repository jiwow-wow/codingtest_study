def solution(s):
    
    answer =[]
    s_list = list(s.split(' '))
    
    for string in s_list:
        for i,c in enumerate(string):
            if i % 2 == 0:
                c = c.upper()
            else: 
                c = c.lower()
            answer.append(c)
        answer.append(' ')
    
    return ''.join(answer)[:-1]