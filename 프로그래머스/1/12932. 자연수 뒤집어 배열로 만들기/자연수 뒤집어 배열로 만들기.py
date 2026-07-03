def solution(n):
    
    num_list = [ int(num) for num in str(n) ]    
    return num_list[::-1]

"""
다른 풀이
return list(map(int, reversed(str(n))))

"""