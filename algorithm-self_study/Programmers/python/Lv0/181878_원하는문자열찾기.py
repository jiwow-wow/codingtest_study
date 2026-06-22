"""
프로그래머스 Lv.0 (기초 15일차-5)

풀이날짜: 2026-06-22
문제번호: 181878
문제명: 원하는 문자열 찾기
링크: https://school.programmers.co.kr/learn/courses/30/lessons/181878

학습내용:
- 

"""


def solution(myString, pat):
    
    if pat.upper() in myString.upper():
        return 1
    else:
        return 0