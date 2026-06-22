"""
프로그래머스 Lv.0 (기초 13일차-2)

풀이날짜: 2026-06-20
문제번호: 181891
문제명: 순서바꾸기
링크: https://school.programmers.co.kr/learn/courses/30/lessons/181891

학습내용:
- 

"""
def solution(num_list, n):
    answer = []
    answer.extend(num_list[n:]+num_list[:n])
    return answer
