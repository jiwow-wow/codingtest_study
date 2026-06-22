"""
프로그래머스 Lv.0 (기초 15일차-4)   

풀이날짜: 2026-06-22
문제번호: 181879    
문제명: 길이에 따른 연산
링크: https://school.programmers.co.kr/learn/courses/30/lessons/181896

학습내용:
- from math import prod 에서 prod(배열) 하면 각 값을 곱한 결과가 나온다
- reduce 라는 함수

"""

from functools import reduce
from math import prod

def solution(num_list):
    
    if len(num_list) >= 11:
        return sum(num_list)
    else:
        # return reduce(lambda x, y: x * y, num_list)
        return prod(num_list)
