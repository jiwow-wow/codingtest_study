"""
프로그래머스 Lv.0 (기초 12일차-2)

문제번호: 181896
문제명: 첫 번째로 나오는 음수
링크: https://school.programmers.co.kr/learn/courses/30/lessons/181896

학습내용:
- 

"""

def solution(num_list):
    answer = -1
    
    for n in num_list:
        if n < 0:
            answer = num_list.index(n)
            break
    
    return answer 

