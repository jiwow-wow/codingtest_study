def solution(myString, pat):
    s_list = []
    
    for i,s in enumerate(list(myString)):
        
        if s == 'A':
            s_list.append('B')
        elif s =='B':
            s_list.append('A')       
            
    return 1 if pat in ''.join(s_list) else 0


'''
replace를 생각했으나, A를 C로 변경해둘 생각을 하지 못했음
int(pat in myString.replace('A', 'C').replace('B', 'A').replace('C', 'B'))
'''