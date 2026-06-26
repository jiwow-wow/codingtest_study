def solution(myStr):
    for s in ['a', 'b', 'c']:
        
        myStr = myStr.replace(s, " ")

    answer = myStr.split()

    return answer if answer else ["EMPTY"]