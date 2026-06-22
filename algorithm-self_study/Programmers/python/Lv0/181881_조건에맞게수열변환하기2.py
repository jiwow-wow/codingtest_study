"""
프로그래머스 Lv.0 (기초 15일차-2)

풀이날짜: 2026-06-22
문제번호: 181881
문제명: 조건에 맞게 수열 변환하기2
링크: https://school.programmers.co.kr/learn/courses/30/lessons/181881

학습내용:
- 

"""
def solution(arr):
    
    x=0
    
    while 1:
        c_arr= []
        for i, n in enumerate(arr):
            if n%2==0 and n >= 50:
                c_arr.append(n//2)
            elif n%2==1 and n < 50:
                c_arr.append(n*2 +1)
            else:
                c_arr.append(n)
        if arr == c_arr:
            break
        x +=1 
        arr = c_arr
        

    return x