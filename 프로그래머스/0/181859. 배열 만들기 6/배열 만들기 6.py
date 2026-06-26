def solution(arr):
    answer = []
    stk= [] #0 1
    i=0
    
    while i < len(arr):
        if len(stk) ==0:
            stk.append(arr[i])
            i +=1
        else:
            
            if stk[-1]==arr[i]:
                stk.pop()
                i +=1
                
            else:
                stk.append(arr[i])
                i+=1
    
    
    return stk  if stk else [-1]