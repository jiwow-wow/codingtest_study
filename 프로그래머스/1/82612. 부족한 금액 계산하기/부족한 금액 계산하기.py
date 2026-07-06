def solution(price, money, count):
    answer = -1
    p_list =[]
    
    for i in range(1, count+1):
        p_list.append(price*i)
        
        
    
    return 0 if sum(p_list) <= money else sum(p_list)-money
    # return abs(min(money - sum([price*i for i in range(1,count+1)]),0))

'''
return max(0,price*(count+1)*count//2-money)
'''