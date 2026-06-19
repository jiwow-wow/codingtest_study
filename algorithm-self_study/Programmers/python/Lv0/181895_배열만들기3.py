"""
프로그래머스 Lv.0 (기초 12일차-3)

풀이날짜: 2026-06-19
문제번호: 181895
문제명: 배열 만들기3
링크: https://school.programmers.co.kr/learn/courses/30/lessons/181895

학습내용:
- 

"""

def solution(arr, intervals):
    answer = []
    
    for i in intervals:
        answer.extend(arr[i[0]:i[1]+1])
    return answer