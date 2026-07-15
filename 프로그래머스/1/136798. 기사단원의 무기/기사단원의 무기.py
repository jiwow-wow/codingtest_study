def solution(number, limit, power):
    
    answer = []
    for n in range(1, number+1):
        factor =[]
        
        for i in range(1,int(n**0.5) +1):
            if n % i ==0 :
                factor.append(n//i)
                factor.append(i)
        answer.append(len(set(factor)))
                    
    
    return sum( [  n if n <= limit else power for n in answer ])

"""
공약수를 구하는 과정에서 중복되는 약수를 set으로 제거

def cf(n): # 공약수 출력
    a = []
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            a.append(n//i)
            a.append(i)
    return len(set(a))
def solution(number, limit, power):
    return sum([cf(i) if cf(i)<=limit else power for i in range(1,number+1)])

"""