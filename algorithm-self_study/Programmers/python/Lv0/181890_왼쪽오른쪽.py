"""
프로그래머스 Lv.0 (기초 13일차-2)

풀이날짜: 2026-06-20
문제번호: 181890
문제명: 왼쪽오른쪽
링크: https://school.programmers.co.kr/learn/courses/30/lessons/181890

학습내용:
- 어떤 리스트의 값과 인덱스를 동시에 사용하려면 for i,s in enumerate(str_list)를 사용할 것

"""
def solution(str_list):
    answer = []
    
    if "l" in str_list or "r" in str_list:
        for i, s in enumerate(str_list):
            if s == "l":
                return str_list[:i]
            elif s == "r":
                return str_list[i+1:]

    
    return answer