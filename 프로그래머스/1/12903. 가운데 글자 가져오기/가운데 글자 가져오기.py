def solution(s):
    mid = len(s)//2
    
    return s[mid] if len(s)%2==1 else s[mid-1:mid+1]
    # return str[(len(str)-1)//2 : len(str)//2 + 1]