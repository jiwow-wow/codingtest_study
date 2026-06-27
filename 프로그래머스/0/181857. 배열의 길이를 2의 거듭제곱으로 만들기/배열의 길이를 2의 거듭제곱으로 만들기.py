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