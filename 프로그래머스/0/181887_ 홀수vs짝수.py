"""
프로그래머스 Lv.0 (기초 14일차-1)

풀이날짜: 2026-06-21
문제번호: 181887
문제명: 홀수vs짝수
링크: https://school.programmers.co.kr/learn/courses/30/lessons/181887

학습내용:
- 

"""

def solution(num_list):
    a_set = sum(num_list[1::2]),sum(num_list[::2])
    print(type(a_set))
    return max(a_set)