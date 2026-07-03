def solution(n):
    
    num_list = sorted([ num for num in str(n)], reverse=True)
    return int(''.join(num_list))