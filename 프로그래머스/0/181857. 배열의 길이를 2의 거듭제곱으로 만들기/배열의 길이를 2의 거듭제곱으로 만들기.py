def solution(arr):
    
    #1번 2의 거듭제곱 리스트 만들어서 in 쓰기
    two_arr = [2**i for i in range(11)]
    
    if len(arr) not in two_arr:
        for k, n in enumerate(two_arr):
            if len(arr) >n and len(arr)< two_arr[k+1]:
                for _ in range(two_arr[k+1] - len(arr)):
                    arr.append(0)
                break
    
    return arr


'''
같은 방법 중 가장 좋은 풀이:
def solution(arr):
    answer = [2**i for i in range(11)]
    while len(arr) not in answer:
        arr.append(0)
    return arr

'''


'''
다른 풀이:
def solution(arr):
    a = 1
    b = len(arr)
    while a < b :
        a *= 2
    return arr + [0] * (a-b)
'''