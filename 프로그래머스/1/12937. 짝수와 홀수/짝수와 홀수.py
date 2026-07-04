def solution(num):
    
    if num%2 ==0:
        return "Even"
    else:
        return "Odd"
    
#     return ["Even", "Odd"][num & 1] #해당 풀이는 비트연산(속도가 빠름)을 통해 마지막 1자리만 연산한다