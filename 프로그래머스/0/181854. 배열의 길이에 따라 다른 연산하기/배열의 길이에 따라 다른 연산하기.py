def solution(arr, n):
    len_arr2 = len(arr)%2
    
    for i, num in enumerate(arr):
        if i%2 != len_arr2:
            arr[i] +=n

    
    return arr