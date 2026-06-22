"""
프로그래머스 Lv.0 (기초 15일차-1)

풀이날짜: 2026-06-22
문제번호: 181882
문제명: 조건에 맞게 수열 변환하기1
링크: https://school.programmers.co.kr/learn/courses/30/lessons/181882

학습내용(+다른 사람의 풀이를 보며 느낀 내용):
- 

"""

def solution(arr):
    
    for i,n in enumerate(arr):
        if n >= 50 and n%2==0:
            arr[i] /= 2
        elif n < 50 and n%2==1:
             arr[i] *=2
    return arr