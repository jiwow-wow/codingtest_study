def solution(t, p):
    answer = 0
    for i in range(len(t) - len(p)+1):
        if t[i:i+len(p)] <=p: #int() 를 쓰지 않아도 사전순으로 비교를 하기 때문에 더 빠름
        # if int(t[i:i+len(p)]) <= int(p):
            answer +=1 
        
    return answer