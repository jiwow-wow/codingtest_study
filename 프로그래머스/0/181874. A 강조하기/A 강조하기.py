def solution(myString):
    str_list = list(myString)
    
    for i,s, in enumerate(str_list):
        if s=='a':
            str_list[i] = s.upper()
        elif s !="A":
            str_list[i] = s.lower()
    
    return ''.join(str_list)