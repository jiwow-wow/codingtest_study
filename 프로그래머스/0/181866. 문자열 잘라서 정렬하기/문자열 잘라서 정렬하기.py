def solution(myString):
    answer = []
    
    # answer.extend(myString.split('x'))
    # answer.sort()
    
    answer = [ s for s in myString.split('x') if s!= '']
    answer.sort()
    
    return answer
#여기서 sorted() 로 한번에 반환가능