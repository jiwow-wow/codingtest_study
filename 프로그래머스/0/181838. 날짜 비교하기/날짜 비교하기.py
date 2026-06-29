def solution(date1, date2):
    
    for i,d1  in enumerate(date1):
        if d1 < date2[i]:
            return 1
        elif date1[i] > date2[i]:
            return 0
    return 0

"""
리스트를 사전식(lexicographical) 으로 비교가능
return int(date1 < date2)
"""