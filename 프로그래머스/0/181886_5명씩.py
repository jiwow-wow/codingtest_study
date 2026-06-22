"""
프로그래머스 Lv.0 (기초 14일차-2)

풀이날짜: 2026-06-21
문제번호: 181886
문제명: 5명씩
링크: https://school.programmers.co.kr/learn/courses/30/lessons/181886

학습내용:
- 

"""

def solution(names):
    answer = []
    for i in range(0, len(names),5):
        answer.append(names[i])
    return answer

'''
최적풀이:4
return names[::5]
'''