"""
프로그래머스 Lv.0 (기초 14일차-5)

풀이날짜: 2026-06-21
문제번호: 181883
문제명: 수열과 구간 쿼리1
링크: https://school.programmers.co.kr/learn/courses/30/lessons/181883

학습내용:
- 

"""

def solution(arr, queries):
    
    for s,e in queries:
        for i in range(s,e+1):
            arr[i] += 1
    return arr